(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21
  const transService = {
   
    queryPayments() {
      toggleUserListLoading();
      return $.ajax({
        url: `${API_ENDPOINT}/payments`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
        
      })
      
        .then((data) => {
          toggleUserListLoading();
          return data;
        })
        .catch((e) => {
          toggleUserListLoading()

          return new $.Deferred().reject(e).promise();
        });
    },

    ledForTrans() {
      return $.ajax({
        url: `${API_ENDPOINT}/ledfortrans`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }

      })

        .then((data) => {
          return data;
        })
        .catch((e) => {

          return new $.Deferred().reject(e).promise();
        });
    },

    queryGrpLedgerById(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/grpledger/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }

      })

        .then((data) => {
          return data;
        })
        .catch((e) => {

          return new $.Deferred().reject(e).promise();
        });
    },

    queryGrpIndLedger(id) {
      // console.log(id)
      return $.ajax({
        url: `${API_ENDPOINT}/grpindled/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }

      })

        .then((data) => {
          return data;
        })
        .catch((e) => {

          return new $.Deferred().reject(e).promise();
        });
    },

    queryindLedger() {
      return $.ajax({
        url: `${API_ENDPOINT}/grpledger`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }

      })

        .then((data) => {
          return data;
        })
        .catch((e) => {

          return new $.Deferred().reject(e).promise();
        });
    },

    getMaxId() {
      return $.ajax({
        url: `${API_ENDPOINT}/transmaxid`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    create(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/transdouble`,
        method: 'POST',
        data: data,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
    },

    update(id, data) {
      return $.ajax({
        url: `${API_ENDPOINT}/trans/${id}`,
        method: 'PUT',
        data: data,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
    }
  }

  $('#add-trans-modal').on('show.bs.modal', function (event) {
    const $ledtag = $('#add-trans-modal').find('#add-ledtag');
    console.log('ledForTrans');
    transService
      .ledForTrans()
      .then(function (result) {
        $ledtag.html("");
        $('#cashbanksel').html("");
        for (grpled in result) {
         if((result[grpled]['is_system'] === "Y" && result[grpled]['cashbank'] === "C") === false){

            $ledtag.append(
              $('<option>').val(result[grpled]['grpledger_id']).text(result[grpled]['name'])
            )
          }else{
            $('#cashbanksel').append(
              $('<option>').val(result[grpled]['grpledger_id']).text(result[grpled]['name'])
            )
          }
        }

        transService
        .queryGrpIndLedger($('#add-ledtag').val())
        .then( function (indres){
            for (indled in indres) {
                $('#add-indled').append(
                  $('<option>').val(indres[indled]['indledger_id']).text(indres[indled]['full_name'])
                ) }
              }
  
        )

        // return transService.queryGrpIndLedger($('#add-ledtag').val());


      })
      // .then((indresdsfd) => {
      //   console.log('And at last', indresdsfd)
      // })
      .catch((e) => {
        console.log('error fetching list');
      });

  });

  $('.input-only-num').on('keypress', function(e){
    return e.metaKey || // cmd/ctrl
    e.which <= 0 || // arrow keys
    e.which == 8 || // delete key
    /[0-9]/.test(String.fromCharCode(e.which)); // numbers
    });

  $('#add-ledtag').change(function() {
    const $addindled = $('#add-trans-modal').find('#add-indled');
    let grpid = $(this).val()
    // var index = this.selectedIndex;
    transService
    .queryGrpLedgerById(grpid)
    .then(function(result){
      
      $addindled.html("");
      if(result['have_subledger'] === "Y"){
        $('#add-indled').prop('disabled', false);
        transService
        .queryGrpIndLedger(grpid)
        .then( function (indres){
            for (indled in indres) {
                $addindled.append(
                  $('<option>').val(indres[indled]['indledger_id']).text(indres[indled]['full_name'])
                ) }
              }

        )

      }else{
        $('#add-indled').prop('disabled', 'disabled');
      }
    })
});

  $(function () {
    const $addModal = $('#add-trans-modal');
    const $editModal = $('#edit-trans-modal');
    const $userListTable = $('#trans-list-table');
    const $reloadUserListBtn = $('#reload-trans-list-btn');
    $('.js-example-basic-single').select2();
    
    // $('#add-indled').prop('disabled', 'disabled');
    $('#datetimepicker1').datepicker();
    $userListTable.on('click', '.edit-btn', handleUserEdit.bind($editModal));

    $addModal
      .find('form')
      .on('submit', openAddModal.bind($addModal));

    $editModal
      .find('form')
      .on('submit', openEditModal.bind($editModal));

    $reloadUserListBtn.on('click', fetchList);

    fetchList()
  });// end document ready

  function toggleUserListLoading() {
    const $el = $('#trans-list-loading');
    const $userListTable = $('#trans-list-table')

    if ($el.css('display') == 'none') {
      $el.css('display', 'block');
      $userListTable.parent().css('display', 'none');
    } else {
      $el.css('display', 'none');
      $userListTable.parent().css('display', 'block');
    }
  }

  function fetchList() {
    // console.log("fetching")
    transService
      .queryPayments()
      .then(function (result) {
        $('#trans-list-table').find('tbody').loadTemplate(
          $('#trans-list-item-tpl'),
          result)
        // console.log("fetching done")
        // console.log(result)
        })
      .catch((e) => {
        console.log('error fetching list');
      });
  }


  function handleUserEdit(evt) {
    const $modal = this;
    const userId = $(evt.target).data('id');

    transService
      .getById(userId)
      .then((user) => {
        $modal.find('input').each((i, input) => {
          const field_name = $(input).attr('name')
          $(input).val(user[field_name])
        })
      });
  }

  function openAddModal(e) {
    e.preventDefault();
    const $modal = this;
    transService.getMaxId()
    .then((maxid)=>{
      maxtransid = maxid['0']
      if(maxtransid === "0") {
        maxtransid = 1
      }
      const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar + '&doc_type=COG'+ '&dr_amt=0' +'&trans_id=' + maxtransid;
      
      transService
        .create(formData)
        .then(() => {
          fetchList()
          $modal.find('form')[0].reset();
          $modal.modal('hide');
        })
        .catch(({ responseJSON: error }) => {
          $modal.find('.error-msg').html(error.message).css('display', 'block');
        });
    })

  }

  function openEditModal(e) {
    e.preventDefault();
    const $modal = this;
    const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar;
    const userId = $modal.find('input[name="trans_id"]').val()

    transService
      .update(userId, formData)
      .then(() => {
        fetchList();
        $modal.modal('hide');
      });
  }

}(jQuery))

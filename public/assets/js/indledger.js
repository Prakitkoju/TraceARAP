(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21

  const indledgerService = {
    query() {
      toggleUserListLoading();
      return $.ajax({
        url: `${API_ENDPOINT}/indledger`,
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

    queryGrpLedger() {
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


    getById(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/indledger/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    createLedgerTag(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/ledgertag`,
        method: 'POST',
        data: data,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
    },

    create(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/indledger`,
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
        url: `${API_ENDPOINT}/indledger/${id}`,
        method: 'PUT',
        data: data,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
    }
  }

  $(function () {
    const $addModal = $('#add-indledger-modal');
    const $editModal = $('#edit-indledger-modal');
    const $userListTable = $('#indledger-list-table');
    const $reloadUserListBtn = $('#reload-indledger-list-btn');

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
    const $el = $('#indledger-list-loading');
    const $userListTable = $('#indledger-list-table')

    if ($el.css('display') == 'none') {
      $el.css('display', 'block');
      $userListTable.parent().css('display', 'none');
    } else {
      $el.css('display', 'none');
      $userListTable.parent().css('display', 'block');
    }
  }

  function fetchList() {

    indledgerService
      .query()
      .then(function (result) {
        $('#indledger-list-table').find('tbody').loadTemplate(
          $('#indledger-list-item-tpl'),
          result)
      })
      .catch((e) => {
        console.log('error fetching list');
      });
  }


  function handleUserEdit(evt) {
    const $modal = this;
    const userId = $(evt.target).data('id');
    console.log("userid", userId);
    indledgerService
      .getById(userId)
      .then((user) => {
        $modal.find('input').each((i, input) => {
          const field_name = $(input).attr('name')
          $(input).val(user[field_name])
        })
      });
  }



  /*

  async function doAsyncWork() {
    try {

      ret_data =  await indlegerService.create(formData)


    } catch {

    }
  }
  */

  function openAddModal(e) {
    e.preventDefault();
    const $modal = this;
    const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar;
    indledgerService
      .create(formData)
      .then(function (retdata)  {
        let bb = retdata['indledger_id']
        // console.log (retdata)
        retdata.indledger_id =  bb
        retdata.grpledger_id =  $("#add-ledtag").val()

        $modal.find('form')[0].reset();
        $modal.modal('hide');

        fetchList();

        // return [
        //   retdata,
          indledgerService.createLedgerTag(retdata)
        //]
        // console.log (retdata)
        //indledgerService.createLedgerTag(retdata)
          // .then(() => {
          // })
          // .catch(({ responseJSON: error }) => {
          //   $modal.find('.error-msg').html(error.message).css('display', 'block');
          // });

        // fetchList()
        // $modal.find('form')[0].reset();
        // $modal.modal('hide');
      })
      // .then((res) => {
        
      // })
      .catch(({ responseJSON: error }) => {
        $modal.find('.error-msg').html(error.message).css('display', 'block');
      });


  }

  // $('#edit-indledger-modal').on('show.bs.modal', function (event) {
  //   const $ledtag = $('#edit-indledger-modal').find('#edit-ledtag');

  //   indledgerService
  //     .queryGrpLedger()
  //     .then(function (result) {
  //       $ledtag.html("");
  //       for (grpled in result) {
  //         // console.log(result[grpled]['name']);
  //         $ledtag.append(
  //           // $('<option>', { value: 1, text: 'One' }),
  //           // $('<option>', { value: 2, text: 'Two' })

  //           // $('<option>').val(result.grpledger_id).text(result.name),
  //           $('<option>').val(result[grpled]['grpledger_id']).text(result[grpled]['name'])
  //         )
  //       }
  //     })
  //     .catch((e) => {
  //       console.log('error fetching list');
  //     });

  // });

  $('#add-indledger-modal').on('show.bs.modal', function (event) {
    const $ledtag = $('#add-indledger-modal').find('#add-ledtag');

    indledgerService
      .queryGrpLedger()
      .then(function (result) {
        $ledtag.html("");
        for (grpled in result) {
          // console.log(result[grpled]['liquidity'] === "Y" && result[grpled]['cashbank'] === "C");
          // if(  (result[grpled]['liquidity'] === "N" && (result[grpled]['cashbank'] === "S" || result[grpled]['cashbank'] === "P")) === false){
          if((result[grpled]['is_system'] === "Y" && result[grpled]['have_subledger'] === "N") ===false){

            $ledtag.append(
              // $('<option>', { value: 1, text: 'One' }),
              // $('<option>', { value: 2, text: 'Two' })
  
              // $('<option>').val(result.grpledger_id).text(result.name),
              $('<option>').val(result[grpled]['grpledger_id']).text(result[grpled]['name'])
            )
          }
        }
      })
      .catch((e) => {
        console.log('error fetching list');
      });

  });

  function openEditModal(e) {
    e.preventDefault();
    const $modal = this;

    const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar;
    const userId = $modal.find('input[name="indledger_id"]').val();

    indledgerService
      .update(userId, formData)
      .then(() => {
        fetchList();
        $modal.modal('hide');
      });
  }

}(jQuery))

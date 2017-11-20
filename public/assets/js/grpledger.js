(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21
  const grpledgerService = {
    query() {
      toggleUserListLoading();
      return $.ajax({
        url: `${API_ENDPOINT}/grpledger`,
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

    getById(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/grpledger/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    create(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/grpledger`,
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
        url: `${API_ENDPOINT}/grpledger/${id}`,
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
    const $addModal = $('#add-grpledger-modal');
    const $editModal = $('#edit-grpledger-modal');
    const $userListTable = $('#grpledger-list-table');
    const $reloadUserListBtn = $('#reload-grpledger-list-btn');

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
    const $el = $('#grpledger-list-loading');
    const $userListTable = $('#grpledger-list-table')

    if ($el.css('display') == 'none') {
      $el.css('display', 'block');
      $userListTable.parent().css('display', 'none');
    } else {
      $el.css('display', 'none');
      $userListTable.parent().css('display', 'block');
    }
  }

  function fetchList() {

    grpledgerService
      .query()
      .then(function (result) {
        $('#grpledger-list-table').find('tbody').loadTemplate(
          $('#grpledger-list-item-tpl'),
          result)
        })
      .catch((e) => {
        console.log('error fetching list');
      });
  }


  function handleUserEdit(evt) {
    const $modal = this;
    const userId = $(evt.target).data('id');

    grpledgerService
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
    const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar;
    grpledgerService
      .create(formData)
      .then(() => {
        fetchList()
        $modal.find('form')[0].reset();
        $modal.modal('hide');
      })
      .catch(({ responseJSON: error }) => {
        $modal.find('.error-msg').html(error.message).css('display', 'block');
      });
  }

  function openEditModal(e) {
    e.preventDefault();
    const $modal = this;
    const formData = $modal.find('form').serialize() + '&user_id=' + user_idvar;
    const userId = $modal.find('input[name="grpledger_id"]').val()

    grpledgerService
      .update(userId, formData)
      .then(() => {
        fetchList();
        $modal.modal('hide');
      });
  }

}(jQuery))

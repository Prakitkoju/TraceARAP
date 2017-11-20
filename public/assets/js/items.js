(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21
  const itemsService = {
    query() {
      toggleUserListLoading();
      return $.ajax({
        url: `${API_ENDPOINT}/items`,
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
        url: `${API_ENDPOINT}/items/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    create(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/items`,
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
        url: `${API_ENDPOINT}/items/${id}`,
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
    const $addModal = $('#add-items-modal');
    const $editModal = $('#edit-items-modal');
    const $userListTable = $('#items-list-table');
    const $reloadUserListBtn = $('#reload-items-list-btn');

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
    const $el = $('#items-list-loading');
    const $userListTable = $('#items-list-table')

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
    itemsService
      .query()
      .then(function (result) {
        $('#items-list-table').find('tbody').loadTemplate(
          $('#items-list-item-tpl'),
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

    itemsService
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
    itemsService
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
    const userId = $modal.find('input[name="item_id"]').val()

    itemsService
      .update(userId, formData)
      .then(() => {
        fetchList();
        $modal.modal('hide');
      });
  }

}(jQuery))

(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21;

  const Service = {
 
    getTrail() {
      console.log('dfd')
      return $.ajax({
        url: `${API_ENDPOINT}/report/trial`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },
 
    getPL() {
      return $.ajax({
        url: `${API_ENDPOINT}/report/pl`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },
 
    getBS() {
      return $.ajax({
        url: `${API_ENDPOINT}/report/bs`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

  }

  $(function () {

      Service
      .getTrail()
      .then(function (result) {
        $('#trans-list-table').find('tbody').loadTemplate(
          $('#trans-list-item-tpl'),
          result)
      })
      .catch((e) => {
        console.log('error fetching list');
      });
  });// end document ready



}(jQuery))

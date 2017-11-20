(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';

  console.log(new URL(location.href))
 

  const userService = {

    search(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/search/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    }

  }

  $(function () {

    console.log("ddddf")
    $('#searchform').on('submit', search);
  });

  function search(e) {
    e.preventDefault();

    const url = new URL(location.href);

    if(!url.pathname.includes('/search')) {
      window.location.href = '/search'+ '?'+ $(this).serialize()
      return;
    }

    //$(location).attr("href", "http://localhost:4000/search")
    let searchstr = $.trim($('#searchby').val());
    if (searchstr != "") {
      userService
        .search(searchstr)
        .then(function (result) {

          $('#trans-search-table').find('tbody').loadTemplate(
            $('#trans-search-item-tpl'),
            result)

        //   $('#trans-search-table').DataTable(
        //     {
        //       data: result,
        //       "columns": [
        //         { "data": "indledger" },
        //         { "data": "grpledger" },
        //         { "data": "dr_amt" },
        //         { "data": "cr_amt" }
        //       ]

        //     }
        //   );

        })
        .catch((e) => {
          console.log('error');
        });
    }


  }

}(jQuery))

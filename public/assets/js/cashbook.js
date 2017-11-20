(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21;

  const Service = {
 
    getCashbook(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/report/cashbook/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    }


  }

  $(function () {
    Service
    .getCashbook(8)
    .then(function (result) {
      // $('#trans-list-table').find('tbody').loadTemplate(
      //   $('#trans-list-item-tpl'),
      //   result)

      $('#trans-list-table').DataTable(
          
        {
          data:result,
          "columns":[
            {"data":"trans_date"},
            {"data":"doc_no"},
            {"data":"grpledger"},
            {"data":"dr_amt"},
            {"data":"cr_amt"},
          ]
            
        }
      );
        

          })
          .catch((e) => {
            console.log('error fetching list');
          });
          
   
     
          // (function(name) {
          //   var container = $('#pagination-' + name);
          //   container.pagination({
          //     dataSource: 'https://api.flickr.com/services/feeds/photos_public.gne?tags=cat&tagmode=any&format=json&jsoncallback=?',
          //     locator: 'items',
          //     totalNumber: 120,
          //     pageSize: 20,
          //     ajax: {
          //       beforeSend: function() {
          //         container.prev().html('Loading data from flickr.com ...');
          //       }
          //     },
          //     callback: function(response, pagination) {
          //       window.console && console.log(22, response, pagination);
          //       var dataHtml = '<ul>';
        
          //       $.each(response, function (index, item) {
          //         dataHtml += '<li>' + item.title + '</li>';
          //       });
        
          //       dataHtml += '</ul>';
        
          //       container.prev().html(dataHtml);
          //     }
          //   })
          // })('demo2');
    
  });// end document ready



}(jQuery))

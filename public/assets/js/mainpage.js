(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';
  const user_idvar = 21;

  const Service = {
    
    getById(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/users/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    getCashBankBalance() {
      return $.ajax({
        url: `${API_ENDPOINT}/cashbankbalance`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      })
      .promise();
      // .then((data) => {
      //   return data;
      // })
      // .catch((e) => {

      //   return new $.Deferred().reject(e).promise();
      // });
      
    },

    update(id, data) {
      return $.ajax({
        url: `${API_ENDPOINT}/users/${id}`,
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
      // Service
      // .getById(user_idvar)
      // .then(function (result) {
       
      //   $('#org_name').text(result.org_name);
      //   $('#org_address').text(result.org_address);
        
      // })
      // .catch((e) => {
      //   console.log('error fetching user list');
      // });
      orgDetail()
     
  });// end document ready

function orgDetail(){
 
  Service
  .getCashBankBalance()
  .then(function (result) {
    for (casbbank in result) {
      if(result[casbbank]['company'] === "company"){
        $('#org_name').text(result[casbbank]['grpledger']);
        $('#org_address').text(result[casbbank]['cashbank']);

      }else{
     if(result[casbbank]['cashbank'] === "C"){
        // bankbalance
        $('#cashbalance').text(result[casbbank]['dr_amt']);
      }else{
        $('#bankbalance').text(result[casbbank]['dr_amt']);
      }
    }
    }
  })
  .catch((e) => {
    console.log('error fetching list');
  });
}

}(jQuery))

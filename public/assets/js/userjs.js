(function ($) {

  const API_ENDPOINT = 'http://localhost:4000/api';

  const userService = {
    
    getById(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/users/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    search(id) {
      return $.ajax({
        url: `${API_ENDPOINT}/search/${id}`,
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
    },

    // getByEmail(email) {
    //   return $.ajax({
    //     url: `${API_ENDPOINT}/users/${email}`,
    //     method: 'GET',
    //     headers: {
    //       'Accept': 'application/json'
    //     }
    //   });
    // },

    create(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/users`,
        method: 'POST',
        data: data,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
    },

    upload(data) {
      return $.ajax({
        url: `${API_ENDPOINT}/upload`,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            //show content
            alert('Success!')
        }
      });
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
    const $signinform = $('#signin-form');
    const $singupform = $('#signup-form');
    const $uploadphoto = $('#upload_photo');

    $signinform
      .on('submit', signin);

    $singupform
      .on('submit', signup);

      $uploadphoto
      .on('submit', uploadFile);

  });// end document ready

  $('#searchbtn').on('click', function(){
    let searchstr = $.trim($('#searchby').val());
    console.log(searchstr);
    if(searchstr != ""){
      userService
      .search(searchstr)
      .then(function (result) {
        $('#trans-list-table').DataTable(
          {
            data:result,
            "columns":[
              {"data":"indledger"},
              {"data":"grpledger"},
              {"data":"dr_amt"},
              {"data":"cr_amt"}
            ]
              
          });
         })
         .catch((e) => {  
           console.log('error');
         });
    }
  })

  function signin(evt) {
    localStorage.loginEmail = $('#loginEmail').val();
    // window.location = "http:localhost:4000/mainpage"
    // alert($(evt.target))
    //  const userId = $(evt.target).data('email');
    userService
    .getById(21)
    .then(function (result) {
         alert ('login with ' + result.email);
         window.location = "/mainpage"
       })
       .catch((e) => {  
         console.log('error');
       });
 

  }

  function signup(e) {
    e.preventDefault();
    const formData = $('#signup-form').serialize();
    userService
      .create(formData)
      .then(() => {
        alert("Sign Up success");
        $('#signup-form').reset();
      })
      
  }

  function uploadFile(e) {
    e.preventDefault();
    console.log('ddd')
    userService
      .upload($('#upload_photo').find('input[name="user_photo"]'))
      
      
  }


  // function signWithEmail(e) {
  //   e.preventDefault();
  //   const formData = $('#signin-form').serialize();
  //   // console.log(formData)
  //   let useremail = formData.split("&", 1);
  //   useremail = useremail[0].replace("email=", "");
  //   useremail = useremail.replace("%40", "@");

  //   let userpass = formData.split("&", 2);
  //   console.log(userpass);
  //   userpass = userpass[1].replace("password=", "");
  //   // console.log(userpass);
  //   userService
  //     .getByEmail(useremail)
  //     .then(()=>{
  //       alert("Sign Up success");
  //       $('#signup-form').reset();
  //     })
  //   userService
  //     .getByEmail(useremail)
  //     .then(()=>{
  //       alert("Sign Up success");
  //       $('#signup-form').reset();
  //     })
      
  // }


}(jQuery))

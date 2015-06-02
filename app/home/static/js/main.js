/**
 * Created by Ted Hill on 15-04-02.
 */
likesCallback = function (authResponse) {
        $('#like_count').html(authResponse.likes);
}
ajaxError = function (authResponse) {
        $('#like_count').html(authResponse.response_reason_text);
}
$('#likes').click(function () {
        catid = $(this).attr("data-catid");
        var keyAuth = {authObject: {
        catid: catid}};
        jsonMsg(keyAuth,likesCallback,'like_category');
});
jsonMsg = function (obj,callBackFunc,url) {
   var authresponse = new Array();
   var json_str = JSON.stringify(obj);
   $.ajax({
       type: "GET",
       url: url,
       dataType   : 'json',
       contentType: 'application/json; charset=UTF-8', // This is the money shot
       data: json_str,
       success: function (msg) {
           try {
               authresponse =  msg;
               callBackFunc(msg)
           } catch (e) {
               authresponse.error = true;
               authresponse.response_reason_text = 'json parse error';
               ajaxError(authresponse)
           }
       },
       error: function (jqXHR, ajaxSettings, thrownError) {
           authresponse.error = true;
           authresponse.response_reason_text = thrownError;
           ajaxError(authresponse)
       }
   });
}


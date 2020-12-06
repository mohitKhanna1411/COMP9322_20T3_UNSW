var running = false;
function send() {
  if (running == true) return;
  var msg = document.getElementById("message").value;
  if (msg == "") return;
  running = true;
  addMsg(msg);
  console.log(msg);
  var url = "http://127.0.0.1:5000/v1/ask?query=" + msg;
  fetch(url) // Call the fetch function passing the url of the API as a parameter
    .then((resp) => resp.json())
    .then(function (data) {
      console.log(data);
      console.log(data["response"].split("\n\n\n"));
      responseArr = data["response"].split("\n");
      for (var i = 0; i < responseArr.length; i++) {
        window.setTimeout(
          addResponseMsg,
          1000 + parseInt(i + "000"),
          responseArr[i]
        );
      }
      // var response = data["response"].replace(/\n/g, "<br />");
      // console.log(response);
      // window.setTimeout(addResponseMsg, 1000, response);
      // window.setTimeout(addResponseMsg, 2000, response);
    })
    .catch(function (error) {
      console.log(error);
    });
}

function addMsg(msg) {
  console.log(msg);
  var div = document.createElement("div");
  div.innerHTML =
    "<span style='flex-grow:1'></span><div class='chat-message'>" +
    msg +
    "</div>";
  div.className = "chat-message-div";
  document.getElementById("message-box").appendChild(div);
  document.getElementById("message").value = "";
}
function addResponseMsg(msg) {
  console.log(msg);
  var div = document.createElement("div");
  div.innerHTML = "<div class='chat-message-response'>" + msg + "</div>";
  div.className = "chat-message-div";
  document.getElementById("message-box").appendChild(div);
  running = false;
}
document.getElementById("message").addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    send();
  }
});

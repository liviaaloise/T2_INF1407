onload = function(){
  document.getElementById('id_username').addEventListener('keyup', verificaUsername)
}

function verificaUsername(e){
  console.log('verificaUsername');
  var campoUsername = document.getElementById('id_username');
  var userName = campoUsername.value;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', '/accounts/verificaUsername' + "?username=" + encodeURIComponent(userName), true);
  xmlhttp.onreadystatechange = verificaUsernameCallBack;
  xmlhttp.send(null);
}

function verificaUsernameCallBack(){
  console.log('callback');
  if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
    var resposta = JSON.parse(xmlhttp.responseText);
    console.log(resposta)
    // if(resposta.existe){
    //   console.log('existe');
    //   document.getElementById('idErro').replaceChild(
    //     document.createTextNode('Esse username já existe'),
    //     document.getElementById('idErro').firstChild
    //   )
    //
    //   var el = document.getElementById('id_username');
    //   el.setAttribute("class","border border-warning");
    //
    // }
    // else{
    //   document.getElementById('idErro').replaceChild(
    //     document.createTextNode('Esse username não existe'),
    //     document.getElementById('idErro').firstChild
    //   )
    //   var el = document.getElementById('id_username');
    //   el.setAttribute("class","");
    //   console.log('nao existe');
    // }
    document.getElementById('idErro').replaceChild(
        document.createTextNode(resposta.mensagem),
        document.getElementById('idErro').firstChild
      );
    document.getElementById('id_username').style = 'border: 2px solid ' + resposta.cor;


  }
}

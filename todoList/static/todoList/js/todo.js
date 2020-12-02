onload = function(e) {
  console.log('onload');
  document.getElementById("minhasTarefas").addEventListener("change", filtraMensagens);

  // setInterval(pegaMensagens, 5000)
}

function filtraMensagens(){
  console.log('Buscando msg');
  // var xmlhttp;
  // xmlhttp = new XMLHttpRequest();
  // xmlhttp.open('GET', '/chat/pegaMensagens', true);
  // xmlhttp.onreadystatechange = function(e) {
  //   if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
  //     var msgs = JSON.parse(xmlhttp.responseText);
  //     if(msgs.length ==0 ) return;
  //
  //     var tabela = document.getElementById('idTableChat');
  //     var novaTabela = document.createElement('table');
  //     novaTabela.setAttribute('id', "idTableChat");
  //     var tr, th, td;
  //     tr = document.createElement('tr');
  //     th = document.createElement('th');
  //
  //     th.appendChild(document.createTextNode('Nickname'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('texto'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('Ip'));
  //     tr.appendChild(th);
  //
  //     novaTabela.appendChild(tr)
  //
  //     for(var i in msgs){
  //       var msg = msgs[i];
  //       tr = document.createElement('tr');
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(msg.nickname));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(msg.texto));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(msg.ipAddress));
  //       tr.appendChild(td);
  //
  //       novaTabela.appendChild(tr);
  //     }
  //
  //     tabela.parentNode.replaceChild(novaTabela, tabela);
  //   }
  };
  xmlhttp.send(null);
}

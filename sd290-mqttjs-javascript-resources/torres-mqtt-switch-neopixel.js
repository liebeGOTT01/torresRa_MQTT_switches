// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')

// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

var broker = 'wss://test.mosquitto.org:8081/mqtt';
var client = mqtt.connect(broker);

var status_header = document.getElementById('status-header')

client.on('connect', function() {
    status_header.innerHTML = 'Connected to ' + broker;
    console.log('Connected to ' + broker)
})

//creating a variable for each switch based on its index
var pub_switch_0 = document.getElementById('pub-switch-0');
var pub_switch_1 = document.getElementById('pub-switch-1');
var pub_switch_2 = document.getElementById('pub-switch-2');

//switch for index[0] that publish the clients request to turn on the light at index 0
pub_switch_0.onclick = () => {
    console.log(pub_switch_0.checked)
    client.publish('cpx-switch/0', String(pub_switch_0.checked))
}

//switch for index[1] that publish the clients request to turn on the light at index 1
pub_switch_1.onclick = () => {
    console.log(pub_switch_1.checked)
    client.publish('cpx-switch/1', String(pub_switch_1.checked))
}

//switch for index[2] that publish the clients request to turn on the light at index 2
pub_switch_2.onclick = () => {
    console.log(pub_switch_2.checked)
    client.publish('cpx-switch/2', String(pub_switch_2.checked))
}
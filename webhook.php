<?php
define('TOKEN', '614721772:AAE0L1O4GgNcurXkddlvd4cQIzgwGP30YqI');

// récupération des données envoyées par Telegram
$content = file_get_contents('php://input');
$update = json_decode($content, true);

// l'utilisateur contacte le bot
if(preg_match('/^\/start/', $update['message']['text'])) {
    sendMessage($update['message']['chat']['id'], 'Bonjour '.$update['message']['from']['username'].' !');
    }

// l'utilisateur envoie la commande : /gps Paris
else if(preg_match('/^\/bonjour/', $update['message']['text'])) {
    $msg = "Bonjour"
    sendMessage($update['message']['chat']['id'], $msg);
    }

// l'utilisateur envoie n'importe nawak
else {
    sendMessage($update['message']['chat']['id'], 'Je n\'ai pas compris.');
    }

// fonction qui envoie un message à l'utilisateur
function sendMessage($chat_id, $text) {
    $q = http_build_query([
        'chat_id' => $chat_id,
        'text' => $text
        ]);
    file_get_contents('https://api.telegram.org/bot'.TOKEN.'/sendMessage?'.$q);
    }
?>

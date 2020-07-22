<?php
//These are the three parameters you can add whatever values you want to add here.
//Also the essay is currently being read from a .txt file you can remove it add whatever form data is recieved.
$essay= htmlentities(readfile("MyCity.txt"));
$category="opinion";
$topic="Environment";
$data= array('essay'=>$essay, 'topic'=>$topic,'category'=>$category);
//This is the url from where the data is extracted.
//Its currently set to localhost but after hosting the app this can be changed.
$host = "http://127.0.0.1:8000";

$url = $host.'/';

echo http($url,$data,'post');
function http($url,$data=[],$method='get'){
    $ch = curl_init();
    $chOpts = [
        CURLOPT_SSL_VERIFYPEER=>false,
        CURLOPT_HEADER=>false,
        CURLOPT_FOLLOWLOCATION=>true,
        CURLOPT_RETURNTRANSFER=>true,
        CURLOPT_CONNECTTIMEOUT =>8,
        CURLOPT_TIMEOUT => 16,
        CURLOPT_HTTPHEADER,[
            'Content-Type: application/json'
        ]
    ];
    if($method=='post'){
        $chOpts[CURLOPT_POST]=true;
        $chOpts[CURLOPT_POSTFIELDS]=$data;
        $chOpts[CURLOPT_URL]=$url;
    }
    else{
        $url.='?'.is_array($data)?http_build_query($data):$data;
        $chOpts[CURLOPT_URL]=$url;
    }
    //here the request data is printed you can remove it if you want only the output.
    echo 'Request: '.$method.'['.$url.']'."\n";
    print_r($data);
    curl_setopt_array($ch, $chOpts);
    $response = curl_exec($ch);
    curl_close($ch);
    echo $response;
    return $response;
}
?>
<?php
//These are the three parameters you can add whatever values you want to add here.
//Also the essay is currently being read from a .txt file you can remove it add whatever form data is recieved.
$myfile = fopen("MyCity.txt", "r") or die("Unable to open file!");
$essay=fread($myfile,filesize("MyCity.txt"));
fclose($myfile);
//$essay= htmlspecialchars(readfile("MyCity.txt"));
//print($essay);
 echo "<br>";
$category="opinion";
$topic="Some people say it is important to keep your home and your workplace tidy, with everything organized and in correct place.";
$data= array('essay'=>$essay, 'topic'=>$topic,'category'=>$category);
//This is the url from where the data is extracted.
//Its currently set to localhost but after hosting the app this can be changed.
$host = "http://127.0.0.1:8000";

$url = $host.'/';
 echo "<br>"; echo "<br>";
 echo "<h1> INPUT --->> </h1>";
echo http($url,$data,'post');
 echo "<br>"; echo "<br>";
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

 echo "<h1> OUTPUT --->> </h1>";
    echo "<br>";
    echo $response;
    return $response;
}
?>
<?php
#retrieve data, columns a list list of column names, sDate is the date to start the search and dure is how far back the user wants to retrieve

function printSQL($sDate, $columns=array('*'), $symbolS=array("googl","rfem","aple"), $dure=1){
	$conn = mysqli_connect("localhost", "keonta", "lovefashion13", "iexcloud");
	$search= join(" ,",$columns);
	$dure = $dure * count($symbolS);
	$symb = "'".$symbolS[0]."'";
	
   foreach ($symbolS as $i){
      if ($i != $symbolS[0]){
         $symb = $symb." OR symbol ='".$i."'";
	  }
   }     
	$query ="SELECT ".$search." FROM master where (symbol = ".$symb.") AND (DATE <='".$sDate."') ORDER BY DATE DESC LIMIT ".(string)$dure;	
	$result = mysqli_query($conn, $query);
	if (!is_bool($result) && mysqli_num_rows($result) > 0) {
		$listOfList = array();
		while($row = mysqli_fetch_assoc($result)) {
			foreach ($row as $key=>$value){
				if ($columns == array('Date')){
						array_push($listOfList, $value);
				}
				else{
				array_push($listOfList, (int)$value);	
				}
			}
	}
}return $listOfList;
}

function printinf($comp){
	$conn = mysqli_connect("localhost", "keonta", "lovefashion13", "iexcloud");    
	$query ="SELECT companyName, description FROM company where (Symbol = '".$comp."')";		
	$result = mysqli_query($conn, $query);
	if (!is_bool($result) && mysqli_num_rows($result) > 0) {
		$listOfList = array();
	while($row = mysqli_fetch_assoc($result)) {
		foreach ($row as $key=>$value){
			array_push($listOfList, $value);	
		}
		}return $listOfList;
	}
	 
}
?>
<?php
function apin($symbols){
$url = "https://cloud.iexapis.com/v1/stock/".$symbols."/chart/1m?filter=close&token=pk_c8a8370e394c49528e4c63007f10c7d1";
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_CONNECTTIMEOUT, 4);
$json = curl_exec($ch);
if(!$json) {
    echo curl_error($ch);
}
curl_close($ch);
$dating =array();
$closing=array();
foreach (json_decode($json) as $row) {
			array_push($dating, (string)date("Y-m-d",strtotime($row->date)));
			array_push($closing,(int)$row->close);
			
}return array($dating,$closing);
}
function apiinf($sym){
$url = "https://cloud.iexapis.com/v1/stock/".$sym."/company/?filter=companyName,description&token=pk_c8a8370e394c49528e4c63007f10c7d1";
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_CONNECTTIMEOUT, 4);
$json = curl_exec($ch);
if(!$json) {
    echo curl_error($ch);
}
curl_close($ch);
$date =array(json_decode($json)->companyName);
$close=array(json_decode($json)->description);
return array($date,$close);		
}
?>
<script>//line
var ctxL = document.getElementById("lineChart").getContext('2d');
document.getElementById("head").innerHTML=<?php echo json_encode(apiinf("googl")[0][0]);?>;
document.getElementById("info").innerHTML=<?php echo json_encode(apiinf("googl")[1][0]);?>;

var mygoogleChart = new Chart(ctxL, {
type: 'line',
data: {
labels: <?php echo json_encode(apin('googl')[0]);?>,
datasets: [{
label: "GOOGL",
data: <?php echo json_encode(apin('googl')[1]);?> ,
backgroundColor: [
'rgba(105, 0, 132, .2)',
],
borderColor: [
'rgba(200, 99, 132, .7)',
],
borderWidth: 2
}
]
},
options: {
responsive: true
}
});
function google(){
document.getElementById("head").innerHTML=<?php echo json_encode(apiinf("googl")[0][0]);?>;
document.getElementById("info").innerHTML=<?php echo json_encode(apiinf("googl")[1][0]);?>;
document.getElementById("sd").innerHTML=<?php echo json_encode(number_format(Stand_Deviation(apin('googl')[1]),2));?>;
document.getElementById("aver").innerHTML=<?php echo json_encode(number_format(array_sum(apin('googl')[1])/count(apin('googl')[1]),2));?>;
	mygoogleChart = new Chart(ctxL, {
type: 'line',
data: {
labels: <?php echo json_encode(apin('googl')[0]);?>,
datasets: [{
label: "GOOGL",
data: <?php echo json_encode(apin('googl')[1]);?> ,
backgroundColor: [
'rgba(105, 0, 132, .2)',
],
borderColor: [
'rgba(200, 99, 132, .7)',
],
borderWidth: 2
}
]
},
options: {
responsive: true
}
});}
function rfem(){
document.getElementById("head").innerHTML=<?php echo json_encode(apiinf("rfem")[0][0]);?>;
document.getElementById("info").innerHTML=<?php echo json_encode(apiinf("rfem")[1][0]);?>;
document.getElementById("sd").innerHTML=<?php echo json_encode(number_format(Stand_Deviation(apin('rfem')[1]),2));?>;
document.getElementById("aver").innerHTML=<?php echo json_encode(number_format(array_sum(apin('rfem')[1])/count(apin('rfem')[1]),2));?>;
mygoogleChart = new Chart(ctxL, {
type: 'line',
data: {
labels: <?php echo json_encode(apin('googl')[0]);?>,
datasets: [{
label: "RFEM",
data: <?php echo json_encode(apin('googl')[1]);?>,
backgroundColor: [
'rgba(0, 140, 124, 0.49)',
],
borderColor: [
'rgba(0, 140, 124, 1)',
],
borderWidth: 2
}
]
},
options: {
responsive: true
}
});
}
function aple(){
document.getElementById("head").innerHTML=<?php echo json_encode(apiinf("aple")[0][0]);?>;
document.getElementById("info").innerHTML=<?php echo json_encode(apiinf("aple")[1][0]);?>;
document.getElementById("sd").innerHTML=<?php echo json_encode(number_format(Stand_Deviation(apin('aple')[1]),2));?>;
document.getElementById("aver").innerHTML=<?php echo json_encode(number_format(array_sum(apin('aple')[1])/count(apin('aple')[1]),2));?>;
mygoogleChart = new Chart(ctxL, {
type: 'line',
data: {
labels: <?php echo json_encode(apin('googl')[0]);?>,
datasets: [{
label: "APLE",
data: <?php echo json_encode(apin('googl')[1]);?>,
backgroundColor: [
'rgba(104, 194, 20, 0.46)',
],
borderColor: [
'rgba(104, 194, 20, 1)',
],
borderWidth: 2
}
]
},
options: {
responsive: true
}
});}
</script>
<?php
function Stand_Deviation($arr) 
    { 
        $num_of_elements = count($arr); 
          
        $variance = 0.0; 
          
                // calculating mean using array_sum() method 
        $average = array_sum($arr)/$num_of_elements; 
          
        foreach($arr as $i) 
        { 
            // sum of squares of differences between  
                        // all numbers and means. 
            $variance += pow(($i - $average), 2); 
        } 
          
        return (float)sqrt($variance/$num_of_elements); 
    } 
?>
<div id='stat'>
	<table class="table">
		  <thead class="black white-text">
			<tr>
			  <th scope="col">Average Close Price Over 30 Days</th>
			  <th scope="col">Standard Deviation from the Average</th>
			</tr>
		  </thead>
		<tbody>
		<tr>
		  <td id="aver"><?php echo number_format(array_sum(apin('googl')[1])/count(apin('googl')[1]),2);?></td>
			<td id="sd"><?php echo number_format(Stand_Deviation(apin('googl')[1]),2);?></td>
		</tr>
		</tbody>
	</table>
</div>

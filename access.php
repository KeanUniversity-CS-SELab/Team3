<?php

#retrieve data, columns a list list of column names, sDate is the date to start the search and dure is how far back the user wants to retrieve
function printSQLs($sDate, $columns=array('*'), $symbolS=array("googl","rfem","aple"), $dure=1){
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
return $listOfList;}
}
?>
<p id="comppar" class="m-3"></p>
<form id="comp" class="m-3" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
	<label for="selcomp">Select computation</label><br>
	<select class="form-control" id="selcomp" name="selcomp" required>
		<option value="min">MIN</option>
		<option value="max">MAX</option>
		<option value="mean">MEAN</option>
	</select><br>
	<label for="compsym">Symbol</label><br>
	<select class="form-control" id="compsym" name="compsym" required>
		<option value="GOOGL">GOOGL</option>
		<option value="RFEM">RFEM</option>
		<option value="APLE">APLE</option>
	</select><br>
	<label for="compstart">Start Date</label><br>
	<input type="date" class="form-control" name="compstart" id="compstart" required max="<?php echo date('Y-m-d'); ?>" min="2014-11-1"><br>
	<label for="compend"> End Date</label><br>
	<input type="date" class="form-control" name="compend" id="compend" required max="<?php echo date('Y-m-d'); ?>" min="2014-11-1"><br>
	<input type="submit" class="btn btn-info btn-block my-4" name="compsub" value="calculate">
</form>
<script>
	function goo(){
		document.getElementById("api").src ="https://cloud.iexapis.com/v1/stock/googl/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1";
		document.getElementById("api").style.display = "block";
	}
	function rfe(){
		document.getElementById("api").src ="https://cloud.iexapis.com/v1/stock/rfem/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1";
		document.getElementById("api").style.display = "block";
	}
	function apl(){
		document.getElementById("api").src ="https://cloud.iexapis.com/v1/stock/aple/chart/1m?token=pk_c8a8370e394c49528e4c63007f10c7d1";
		document.getElementById("api").style.display = "block";
	}
</script>
<?php

if(isset($_POST["compsub"])){
	$calcdure = (strtotime($_POST["compend"])-strtotime($_POST["compstart"]))/86400;
	$arr = printSQLs(date("Y-m-d",strtotime($_POST["compend"])),$columns=array('Close'),$symbolS=array($_POST["compsym"]), $dure=$calcdure);
	 if ($_POST["selcomp"]=="max"){
		?>
		<script>
			 document.getElementById("comppar").innerHTML=<?php echo json_encode("The max price for ".$_POST["compsym"]." for the dates between ".$_POST["compstart"]." and ".$_POST["compend"]." is ".max($arr));?>; 
		</script>
		<?php
		}
	if ($_POST["selcomp"]=="min"){
		?>
		<script>
			document.getElementById("comppar").innerHTML=<?php echo json_encode("The min price for ".$_POST["compsym"]." for the dates between ".$_POST["compstart"]." and ".$_POST["compend"]." is ".min($arr));?>;
		</script>
		<?php
		}
	if ($_POST["selcomp"]=="mean"){
		?>
		<script>
			document.getElementById("comppar").innerHTML=<?php echo json_encode("The mean price for ".$_POST["compsym"]." for the dates between ".$_POST["compstart"]." and ".$_POST["compend"]." is ".array_sum($arr)/count($arr));?>;
		</script>
		<?php
		} 	

}



?>
<div class="text-center">

  <button type="button" class="btn btn-info" data-toggle="modal" data-target="#modalYT" onclick="goo()">GOOGL</button>
  <button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalYT" onclick="rfe()">RFEM</button>
  <button type="button" class="btn btn-secondary" data-toggle="modal" data-target="#modalYT" onclick="apl()">APL</button>

</div>

<!--Modal: Name-->
<div class="modal fade" id="modalYT" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" role="document">

    <!--Content-->
    <div class="modal-content">

      <!--Body-->
      <div class="modal-body mb-0 p-0">

        <div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
          <iframe class="embed-responsive-item" id="api" src="" style="display:none;"></iframe>
        </div>

      </div>

      <!--Footer-->
      <div class="modal-footer justify-content-center">
        <button type="button" class="btn btn-outline-primary btn-rounded btn-md ml-4" data-dismiss="modal">Close</button>

      </div>

    </div>
    <!--/.Content-->

  </div>
</div>

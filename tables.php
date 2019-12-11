<style>
.my-custom-scrollbar {
position: relative;
height: 30vw;
overflow: auto;
}
.table-wrapper-scroll-y {
display: block;
}
</style>
<?php
$conn = mysqli_connect("localhost", "keonta", "lovefashion13", "iexcloud");
$sql1 = "SELECT * FROM master ORDER BY DATE DESC LIMIT 30";
$results = mysqli_query($conn, $sql1);
?>

<!-- Table with panel -->
<div class="card card-cascade narrower">

  <!--Card image-->
  <div
    class="view view-cascade gradient-card-header blue-gradient narrower py-2 mx-4 mb-3 d-flex justify-content-between align-items-center">



    <a href="" class="white-text mx-3">30 DAY RECORDS</a>

  </div>
  <!--/Card image-->

  <div class="px-4">

    <div class="table-wrapper-scroll-y my-custom-scrollbar">
      <!--Table-->
      <table id="dtBasicExample" class="table table-hover mb-0 table-striped table-bordered table-sm" cellspacing="0" width="30vw">

        <!--Table head-->
        <thead>
          <tr>
            <th class="th-lg">
              <a>DATE
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>SYMBOL
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>VOLUME
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>OPEN
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>CLOSE
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>HIGH
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
            <th class="th-lg">
              <a>LOW
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
			 <th class="th-lg">
              <a>x
                <i class="fas fa-sort ml-1"></i>
              </a>
            </th>
          </tr>
        </thead>
        <!--Table head-->

        <!--Table body-->
        <tbody>
		<?php
		if (mysqli_num_rows($results) > 0) {
			while($row = mysqli_fetch_assoc($results)) {
				echo "<tr><td>". $row["Date"]."</td>"."<td>". $row["symbol"]."</td>"."<td>". $row["Volume"]."</td>"."<td>". $row["Open"]."</td>"."<td>". $row["Close"]."</td>"."<td>". $row["High"]."</td>"."<td>". $row["Low"]."</td></tr>";
			}
		}?>
           
        </tbody>
        <!--Table body-->
      </table>
      <!--Table-->
    </div>

  </div>

</div>

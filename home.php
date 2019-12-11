

<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.11/css/mdb.min.css" rel="stylesheet">
<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
<?php include('nav.php'); ?>
<div class="content-container">
	<ul class="nav nav-tabs" id="myTab" role="tablist">
	  <li class="nav-item">
		<a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home"
		  aria-selected="true">Symbol Chart</a>
	  </li>
	  <li class="nav-item">
		<a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile"
		  aria-selected="false">Symbol Table</a>
	  </li>
	  <li class="nav-item">
		<a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact"
		  aria-selected="false">Changes</a>
	  </li>
	</ul>
	<div class="tab-content" id="myTabContent">
	  <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab"><?php include('lineChart.php'); ?></div>
	  <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab"><?php include('tables.php');?></div>
	  <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab"><!-- Default form register -->
		<?php include("access.php")?>
<!-- Default form register --></div>
	</div>



</div>
<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js" type="text/javascript"></script>
<script src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js" type="text/javascript"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.11/js/mdb.min.js"></script>
<script src="https://kit.fontawesome.com/d99fb3df37.js" crossorigin="anonymous"></script>
<?php include('js/chart.php');?>
<script>
// Basic example
$(document).ready(function(){
$('#dtBasicExample').DataTable({
	columnDefs: [ {
				orderable: false,
				className: 'select-checkbox',
				targets:   0
			} ],
			select: {
				style:    'os',
				selector: 'td:first-child'
			},
			//order: [[ 1, 'asc' ]]
		} );
$('.dataTables_length').addClass('bs-select');
	
});

</script>
<html>
	<head>
		<title>Pizza Orders Management</title>
		<style type="text/css">
			.pizza {
				font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
				border-collapse: collapse;
				width: 50%;
				margin: auto;
			}

			.pizza td, .pizza th {
				border: 1px solid #ddd;
				padding: 8px;
			}

			.pizza tr:hover {background-color: #ddd;}

			.pizza th {
				padding-top: 12px;
				padding-bottom: 12px;
				text-align: left;
				background-color: #0000FF;
				color: white;
			}
			
			.button:hover{
				cursor: hand;
			}
		</style>
		
	</head>
	<body>
		<script type="text/javascript">
			function updateOrder(object){
				var http = new XMLHttpRequest();
				var params = "id:"+object.id.substring(6,object.id.length)+"&status:"+document.getElementById("orderstatus"+object.id.substring(6,object.id.length)).value;
				var url = "/updatepizza/"+params;
				
				http.open("GET", url, true);

				//Send the proper header information along with the request
				http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

				http.onreadystatechange = function() {//Call a function when the state changes.
					if(http.readyState == 4 && http.status == 200) {
						alert("Status updated successfully.");
						location.reload(true);
					}
				}
				http.send();
			}
			
			function deleteOrder(object){
				var http = new XMLHttpRequest();
				var params = object.id.substring(6,object.id.length);
				var url = "/deletepizza/"+params;
				
				http.open("GET", url, true);

				//Send the proper header information along with the request
				http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

				http.onreadystatechange = function() {//Call a function when the state changes.
					if(http.readyState == 4 && http.status == 200) {
						alert("Order deleted successfully.");
						location.reload(true);
					}
				}
				http.send();
			}
		</script>
		
		<h2 align="center">Pizza Order Management System</h2>
		
		<form action="/addpizza" method="post">
			<table class="pizza">
				<tr>
					<th colspan="2">Add New Order</th>
				</tr>
				<tr>
					<td>Order ID:</td>
					<td><input type="text" id="orderid" name="orderid" style="width:90%"/></td>
				</tr>
				<tr>
					<td>Status:</td>
					<td><select id="orderstatus" name="orderstatus" style="width:90%">
						<option value="1">Order Confirmed</option>
						<option value="2">Pizza Prepared</option>
						<option value="3">Pizza Baked</option>
						<option value="4">Pizza On the Way</option>
						<option value="5">Pizza Delivered</option>
					</select></td>
				</tr>
				<tr>
					<td colspan="2" align="center"><input type="submit" value="Add New Order"/></td>
				</tr>
			</table>		
		</form>
		<form method="post">
			<table class="pizza">
				<tr>
					<th colspan="4">Order Details</th>
				</tr>
				<tr>
					<th>Order ID</td>
					<th>Status</td>
					<th>Update</td>
					<th>Delete</td>
				</tr>
				%for order in sorted(rows.keys()):
				<tr>
					<td>
						<label>{{order}}</label>
					</td>
					<td><select id="orderstatus{{order}}">
						%if(rows[order]==1):
							<option value="1" selected="true">Order Confirmed</option>
						%else:
							<option value="1">Order Confirmed</option>
						%end
						%if(rows[order]==2):
							<option value="2" selected="true">Pizza Prepared</option>
						%else:
							<option value="2">Pizza Prepared</option>
						%end
						%if(rows[order]==3):
							<option value="3" selected="true">Pizza Baked</option>
						%else:
							<option value="3">Pizza Baked</option>
						%end
						%if(rows[order]==4):
							<option value="4" selected="true">Pizza On the Way</option>
						%else:
							<option value="4">Pizza On the Way</option>
						%end
						%if(rows[order]==5):
							<option value="5" selected="true">Pizza Delivered</option>
						%else:
							<option value="5">Pizza Delivered</option>
						%end
					</select></td>
					<td><img onclick="updateOrder(this)" class="button" id="update{{order}}" src="/static/update.png" height="30" width="30"/></td>
					<td><img onclick="deleteOrder(this)" class="button" id="delete{{order}}" src="/static/delete.png" height="30" width="30"/></td>
				</tr>
				%end
			</table>
		</form>
	</body>
</html>
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
		<h2 align="center">Pizza Order Management System</h2>
		
		<form action="/getpizza" method="post">
			<table class="pizza">
				<tr>
					<th colspan="2">Check Order Status</th>
				</tr>
				<tr>
					<td>Order ID:</td>
					<td><input type="text" id="orderid" name="orderid" style="width:90%"/></td>
				</tr>
				<tr>
					<td colspan="2" align="center"><input type="submit" value="Get Status"/></td>
				</tr>
			</table>		
		</form>
		<br/><br/><br/><br/>
		%for row in rows:
			%print(row[0])
			%if(row[0]==None):
				<table style="width:70%;height:10%;font:calibri" align="center">
					<tr style="width:70%;text-align:center;">
						<td style="border:1px solid green;">Order is not valid</td>
					</tr>
				</table>
			%else:
				%status = int(row[1])
					<table style="width:70%;height:10%;font:calibri" align="center">
						<tr style="width:70%;text-align:center;">
							%if(status>=1):
								<td style="width:20%;border:1px solid green;background-color:green;color:white;font-weight:bold;">Order Confirmed</td>
							%else:
								<td style="width:20%;border:1px solid green;">Order Confirmed</td>
							%end
							%if(status>=2):
								<td style="width:20%;border:1px solid green;background-color:green;color:white;font-weight:bold;">Pizza Prepared</td>
							%else:	
								<td style="width:20%;border:1px solid green;">Pizza Prepared</td>
							%end
							%if(status>=3):
								<td style="width:20%;border:1px solid green;background-color:green;color:white;font-weight:bold;">Pizza Baked</td>
							%else:	
								<td style="width:20%;border:1px solid green;">Pizza Baked</td>
							%end
							%if(status>=4):
								<td style="width:20%;border:1px solid green;background-color:green;color:white;font-weight:bold;">Pizza On the Way</td>
							%else:
								<td style="width:20%;border:1px solid green;">Pizza On the Way</td>
							%end
							%if(status>=5):
								<td style="width:20%;border:1px solid green;background-color:green;color:white;font-weight:bold;">Pizza Delivered</td>
							%else:
								<td style="width:20%;border:1px solid green;">Pizza Delivered</td>
							%end
						</tr>
					</table>
			%end
		%end
	</body>
</html>
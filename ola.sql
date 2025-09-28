use ola_project;
/*1.  Retrieve all successful bookings*/
select * from rides
where Booking_Status="Success";

/*2.   Find the average ride distance for each vehicle types*/
select Vehicle_Type, avg(Ride_Distance) as AVG_Ride_Distance
from rides 
group by Vehicle_Type;

/*3. Total cancelled rides by customers*/
ALTER TABLE rides
MODIFY COLUMN Canceled_Rides_by_Customer VARCHAR(255);
SELECT COUNT(*) AS Total_Cancelled_By_Customer
FROM rides
WHERE Canceled_Rides_by_Customer != '0';

/*4. Top 5 customers by number of bookings*/

select Customer_ID, count(*) as Total_rides
from rides
group by Customer_ID
order by Total_rides desc
limit 5;

/*5. Number of rides cancelled by drivers due to personal/car issues*/

select count(*) As canceled_rides_by_driver
from rides
where Canceled_Rides_by_Driver="Personal & Car related issue";

/*6. Maximum and minimum driver ratings for Prime Sedan bookings*/

SELECT MAX(Driver_Ratings) AS Max_Driver_Rating,
       MIN(Driver_Ratings) AS Min_Driver_Rating
FROM rides
WHERE Vehicle_Type = 'Prime Sedan';

/*7. Retrieve all rides where payment was made using UPI*/
SELECT *
FROM rides
WHERE Payment_Method = 'UPI';

/*8.Average customer rating per vehicle type*/

SELECT Vehicle_Type, 
       AVG(Customer_Rating) AS Avg_Customer_Rating
FROM rides
GROUP BY Vehicle_Type;

/* 9. Total booking value of rides completed successfully*/
SELECT SUM(Booking_Value) AS Total_Booking_Value
FROM rides
WHERE Booking_Status = 'Success';

/*10. List all incomplete rides along with the reason*/
SELECT Booking_ID, Incomplete_Rides, Incomplete_Rides_Reason
FROM rides
WHERE Incomplete_Rides != 'NA';

/*Total rides & success rate*/
SELECT Booking_Status, COUNT(*) 
FROM rides 
GROUP BY Booking_Status;

/*Revenue trend*/

SELECT DATE(Date) AS ride_date, SUM(Booking_Value) AS daily_revenue
FROM rides
GROUP BY ride_date
ORDER BY ride_date;

/*Top 5 locations*/

SELECT Pickup_Location, COUNT(*) AS ride_count
FROM rides
GROUP BY Pickup_Location
ORDER BY ride_count DESC
LIMIT 5;







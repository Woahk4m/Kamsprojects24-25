// See https://aka.ms/new-console-template for more information
using System;

class Program
{
    // Private instance variables
    private float myNum;
    public int myNum2;

    // Array for ticket prices
    private float[] ticketPrices = { 10.0F, 15.0F, 20.0F, 25.0F, 30.0F }; // Example prices

    // Public method to initialize values
    public void InitializeValues()
    {
        myNum = 10.0F;  // Float variable for speed
        myNum2 = 60;    // Integer for ticket count

        Console.WriteLine("Hellooooo, RACERSSSSSSSS!");
        Console.WriteLine("ON YOUR MARKS");
        Console.WriteLine("GET SET");
        Console.WriteLine("GO...!!!");

        Console.WriteLine(myNum);   // Print myNum
        Console.WriteLine(myNum2);   // Print myNum2

        // For loop to print ticket numbers
        for (int count = 0; count < 5; count++)
        {
            Console.WriteLine("Ticket number " + (count + 1)); // Consistent casing
        }

        // Check if myNum is greater than 100
        if (myNum > 100.00)
        {
            Console.WriteLine("YOU WERE GOING OVER 100 MPH?");
        }
        else
        {
            Console.WriteLine("Phew, you were going under 100 mph.");
        }

        // Check if myNum2 is greater than 20
        if (myNum2 > 20)
        {
            Console.WriteLine("THERE'S MORE THAN 20 TICKETS?! HOW'S THAT POSSIBLE?"); // Fixed grammar
        }
        else
        {
            Console.WriteLine("Okay, good, it's less than 20 tickets.");
        }

        Console.WriteLine("Ticket Prices: ");
        for (int i = 0; i < ticketPrices.Length; i++) // Fixed array access and loop variable
        {
            Console.WriteLine($"Ticket {i + 1}: ${ticketPrices[i]}");    
        }
    }

    // Main method
    public static void Main()
    {
        Program program = new Program(); // Create an instance of Program
        program.InitializeValues();       // Initialize values and display messages
    }
}
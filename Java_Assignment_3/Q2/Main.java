public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter distance in meters: ");
        double meters = scanner.nextDouble();

        DistanceConverter converter = new DistanceConverter();
        
        System.out.println(meters + " meters is equal to " + converter.toKilometers(meters) + " kilometers.");
        System.out.println(meters + " meters is equal to " + converter.toCentimeters(meters) + " centimeters.");
        System.out.println(meters + " meters is equal to " + converter.toMillimeters(meters) + " millimeters.");
        
        scanner.close();
    }
}
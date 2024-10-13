public class Main {
    public static void main(String[] args) {
        // Creating a Car object
        Car car = new Car("Toyota", "Corolla", 2012);

        // Creating a Person object
        Person person = new Person("John", 30, car);

        // Printing the information of the car and the person using the getInfo() method
        System.out.println(car.getInfo());
        System.out.println(person.getInfo());
    }
}

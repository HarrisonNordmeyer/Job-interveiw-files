public class Main {

    public static void main(String[] args) {
        
        // Creating book objects using different constructors
        Book book1 = new Book("The Alchemist", "Paulo Coelho", 1988);
        Book book2 = new Book("The Alchemist", "Paulo Coelho");
        Book book3 = new Book("1984");
        
        // Displaying book details
        book1.displayBookDetails();
        book2.displayBookDetails();
        book3.displayBookDetails();
    }
}

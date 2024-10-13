public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        
        int[] arr = new int[n];
        
        for(int i = 0; i < n; i++) {
            System.out.print("Enter element " + (i + 1) + ": ");
            arr[i] = scanner.nextInt();
        }
        
        ArrayManipulator manipulator = new ArrayManipulator();
        
        System.out.println("Minimum: " + manipulator.findMin(arr));
        System.out.println("Maximum: " + manipulator.findMax(arr));
        System.out.println("Average: " + manipulator.findAverage(arr));
        
        int[] doubledArray = manipulator.doubleElements(arr);
        
        System.out.print("Doubled Array: ");
        for(int elem : doubledArray) {
            System.out.print(elem + " ");
        }

        scanner.close();
    }
}

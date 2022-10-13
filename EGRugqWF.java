import java.util.Scanner;
import java.util.HashSet;

public class BubbleSort{
    // 交換a和b
    public static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    public static void main(String args[]){
        int arrLen = (int)((Math.random()*100)+1);
        // 產生不重複Array
        int arr[] = new int[arrLen];
        HashSet<Integer> book = new HashSet<Integer>(); //用集合去判斷是否重複
        for (int ar=0; ar<arrLen; ar++) {
            int rng = (int)((Math.random()*100)+1);
            if (!book.contains(rng)){
                arr[ar] = rng;
                book.add(rng);
            }
            else ar-=1;
        }
        Scanner scn = new Scanner(System.in);
        boolean n = scn.nextInt() == 1?true:false;
        for (int i=0; i<arr.length; i++) {
            for (int j=0; j<arr.length-i-1; j++) {
                if(!(n ^ (arr[j] > arr[j+1]))){
                    swap(arr, j, j+1);
                }
            }
        }
        for (int k=0; k<arr.length; k++) System.out.printf("%d ", arr[k]);
        System.out.println("");
    }
}

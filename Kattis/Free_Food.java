public class Free_Food{
  public static void main(String[] args){
    java.util.Scanner sc = new java.util.Scanner(System.in);
    int cs  = sc.nextInt();
    java.util.ArrayList<Integer> d = new java.util.ArrayList<>();
    for(int i = 0; i < cs; i++){
      int s = sc.nextInt();
      int e = sc.nextInt();
      for(int j = e; j > s - 1; j--){
        if(d.indexOf(j) == -1){
          d.add(j);
        }
      }
    }
    System.out.println(d.size());
    sc.close();
  }
}

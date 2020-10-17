class Dice_Cup{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int d1 = sc.nextInt(), d2 = sc.nextInt();
        java.util.ArrayList<Integer> sums = new java.util.ArrayList<>();
        for(int i = 1; i <= d1; i++){
            for(int j = 1; j <= d2; j++){
                sums.add(i + j);
            }
        }
        java.util.ArrayList<Integer> check = new java.util.ArrayList<>();
        java.util.ArrayList<Sum> values = new java.util.ArrayList<>();
        for(Integer i: sums){
            if(check.indexOf(i) == -1){
                check.add(i);
                Sum s = new Sum(i);
                s.sum();
                values.add(s);
            }else{
                for(Sum s: values){
                    if(s.value == i)s.sum();
                }
            }
        }
        int max = 0;
        for(Sum s: values){
            if(s.count > max){
                max = s.count;
                // value = s.value;
            }
        }
        for(Sum s: values){
            if(s.count == max){
                System.out.println(s.value);
            }
        }
        sc.close();
    }
}

class Sum{
    int count = 0;
    int value;

    Sum(int value){
        this.value = value;
    }

    void sum(){
        count++;
    }
}

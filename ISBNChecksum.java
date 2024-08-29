public class ISBNChecksum
{
    public static void main(String[] args)
    {
      if(args.length==1){
          int count = 0;
 
        String s = args[0];
 
        for (int i = 1; i < 10; i++){
            count += (i*(s.charAt(i-1)-'0'));
        }
 
        count = count % 11;
 
        if(count < 10){
            System.out.println(count);
        }
        else{
            System.out.println("X");
        }
      }
      else{
          System.out.println("Error");
      }
    }
}
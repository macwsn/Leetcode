class CustomStack {
    private static int[] tab;
    private int maxSize;
    private static int counter;

    public CustomStack(int maxSize) {
        tab = new int[maxSize];
        counter = 0;
        this.maxSize = maxSize;
    }
    
    public void push(int x) {
        if(counter < maxSize){
            tab[counter] = x;
            counter++;
        }
    }
    
    public int pop() {
        if(counter == 0){
            return -1;
        }
        else{
            counter--;
            return tab[counter];
        }
    }
    
    public void increment(int k, int val) {
        for(int i=0;i<Math.min(k,counter);i++){
            tab[i]+=val;
        }
    }
}

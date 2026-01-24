class Solution {
public:
    int climbStairs(int m, vector<int>& costs) {
        int n = costs.size();
        std::vector<int> tab(n+1, 0);
        tab[1] = costs[0] + 1;
        if(n < 2){
            return tab[1];
        }
        tab[2] = costs[1] + std::min(tab[1] + 1,4);
        if(n<3){
            return tab[2];
        }
        tab[3] = costs[2] + std::min(9, std::min(4 + tab[1], 1 + tab[2]));
        if(n<4){
            return tab[3];
        }
        for(int i=4;i<n+1;i++){
            tab[i] = costs[i-1] + min(9 + tab[i-3],std::min( 4 + tab[i-2], 1 + tab[i-1]));
        } 
        return tab[n];
    }
};
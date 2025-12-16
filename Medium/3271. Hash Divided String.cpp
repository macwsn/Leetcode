class Solution {
public:
    string stringHash(string s, int k) {
        const int n = s.length();
        const int size = n / k;
        int sum;
        std::string res(size,'0');
        for(int i=0;i<size;i++){
            sum = 0;
            for(int j=0;j<k;j++){
                sum += (int(s[i*k+j])-97);
                sum %= 26;
            }
            res[i] = char(sum + 97);
        }
        return res;
    }
};
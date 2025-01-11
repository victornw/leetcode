class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      ans = []
      base = []
      for s in strs:
         if(sorted(s) in base):
            ans[base.index((sorted(s)))].append(s)

         else:
            ans.append([s])
            base.append(sorted(s))
      return ans
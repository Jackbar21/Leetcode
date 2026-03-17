class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (char c : s.toCharArray())
        {
            sMap.put(c, 1 + sMap.getOrDefault(c, 0));
        }

        for (char c : t.toCharArray())
        {
            tMap.put(c, 1 + tMap.getOrDefault(c, 0));
        }

        return sMap.equals(tMap);
    }
}
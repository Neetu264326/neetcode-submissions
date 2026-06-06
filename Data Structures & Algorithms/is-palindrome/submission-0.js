class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let cleaned = "";

        for (let ch of s) {
            if (/[a-zA-Z0-9]/.test(ch)) {
                cleaned += ch.toLowerCase();
            }
        }

        return cleaned === cleaned.split('').reverse().join('');
    }
}
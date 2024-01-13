<h2><a href="https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/">1347. Minimum Number of Steps to Make Two Strings Anagram</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53" data-immersive-translate-paragraph="1">You are given two strings of the same length <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">s</code> and <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code>. In one step you can choose <strong data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">any character</strong> of <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code> and replace it with <strong data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">another character</strong>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得兩個長度 <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">s</code> 相同且 <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code> 相同的字串。在一個步驟中，您可以選擇任何 <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code> 字元並將其替換為另一個字元。</font></font></font></p>

<p data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">the minimum number of steps</em> to make <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code> an anagram of <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">s</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回使 <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">t</code> 字謎的 <code data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">s</code> 最小步數。</font></font></font></p>

<p data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53" data-immersive-translate-paragraph="1">An <strong data-immersive-translate-walked="f26d734e-d734-4a6c-af3a-7db6d0ceca53">Anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">字串的字謎是包含具有不同（或相同）順序的相同字元的字串。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "bab", t = "aba"
<strong>Output:</strong> 1
<strong>Explanation:</strong> Replace the first 'a' in t with b, t = "bba" which is anagram of s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "leetcode", t = "practice"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "anagram", t = "mangaar"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "anagram" and "mangaar" are anagrams. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s.length == t.length</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters only.</li>
</ul>
</div>
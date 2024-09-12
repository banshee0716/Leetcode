<h2><a href="https://leetcode.com/problems/count-the-number-of-consistent-strings/">1684. Count the Number of Consistent Strings</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488" data-immersive-translate-paragraph="1">You are given a string <code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">allowed</code> consisting of <strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">distinct</strong> characters and an array of strings <code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">words</code>. A string is <strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">consistent </strong>if all characters in the string appear in the string <code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">allowed</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給您一個<code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">allowed</code>由<strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">不同</strong>字元和<code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">words</code>陣列組成的字串。如果字串中的所有字元都出現在<code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">allowed</code>字串中，則該字串是<strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">一致的</strong>。</font></font></font></p>

<p data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488" data-immersive-translate-paragraph="1">Return<em data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488"> the number of <strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">consistent</strong> strings in the array </em><code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">words</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回數組<code data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">words</code><em data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">中<strong data-immersive-translate-walked="6b031f46-e945-4f0b-b3d7-a98b75ce9488">一致</strong>字串的數量</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All strings are consistent.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Strings "cc", "acd", "ac", and "d" are consistent.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= allowed.length &lt;=<sup> </sup>26</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li>The characters in <code>allowed</code> are <strong>distinct</strong>.</li>
	<li><code>words[i]</code> and <code>allowed</code> contain only lowercase English letters.</li>
</ul>
</div>
<h2><a href="https://leetcode.com/problems/palindrome-partitioning/">131. Palindrome Partitioning</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913" data-immersive-translate-paragraph="1">Given a string <code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code>, partition <code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code> such that every <span data-keyword="substring-nonempty" data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">substring</span> of the partition is a <span data-keyword="palindrome-string" data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913"><strong data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">palindrome</strong></span>. Return <em data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">all possible palindrome partitioning of </em><code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個字串 <code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code> ，對 <code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code> 進行分區，使得分割區的每個子字串都是回文。傳回 <code data-immersive-translate-walked="8e5eb946-ff1f-437e-8a6d-9d78829d5913">s</code> 所有可能的回文分割區。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
</div>
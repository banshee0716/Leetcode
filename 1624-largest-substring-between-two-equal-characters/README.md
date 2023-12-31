<h2><a href="https://leetcode.com/problems/largest-substring-between-two-equal-characters/">1624. Largest Substring Between Two Equal Characters</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f" data-immersive-translate-paragraph="1">Given a string <code data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">s</code>, return <em data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">the length of the longest substring between two equal characters, excluding the two characters.</em> If there is no such substring return <code data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">-1</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個字串，返回兩個相等字元之間最長子字串 <code data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">s</code> 的長度，不包括這兩個字元。如果沒有這樣的子字串，則傳回 <code data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">-1</code> 。</font></font></font></p>

<p data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="94d5041b-2bf3-4593-b8de-e30679bc669f">substring</strong> is a contiguous sequence of characters within a string.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">子字串是字串中連續的字元序列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aa"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The optimal substring here is an empty substring between the two <code>'a's</code>.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abca"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The optimal substring here is "bc".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "cbzxy"
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no characters that appear twice in s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
</div>
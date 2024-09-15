<h2><a href="https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/">1371. Find the Longest Substring Containing Vowels in Even Counts</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="aad29e69-4150-4e57-9b7f-fa69e5eb970b" data-immersive-translate-paragraph="1">Given the string <code data-immersive-translate-walked="aad29e69-4150-4e57-9b7f-fa69e5eb970b">s</code>, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定字串<code data-immersive-translate-walked="aad29e69-4150-4e57-9b7f-fa69e5eb970b">s</code> ，傳回包含每個母音偶數次的最長子字串的大小。也就是說，「a」、「e」、「i」、「o」和「u」必須出現偶數次。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "eleetminicoworoep"
<strong>Output:</strong> 13
<strong>Explanation: </strong>The longest substring is "leetminicowor" which contains two each of the vowels: <strong>e</strong>, <strong>i</strong> and <strong>o</strong> and zero of the vowels: <strong>a</strong> and <strong>u</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "leetcodeisgreat"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is "leetc" which contains two e's.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "bcbcbc"
<strong>Output:</strong> 6
<strong>Explanation:</strong> In this case, the given string "bcbcbc" is the longest because all vowels: <strong>a</strong>, <strong>e</strong>, <strong>i</strong>, <strong>o</strong> and <strong>u</strong> appear zero times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 x 10^5</code></li>
	<li><code>s</code>&nbsp;contains only lowercase English letters.</li>
</ul>
</div>
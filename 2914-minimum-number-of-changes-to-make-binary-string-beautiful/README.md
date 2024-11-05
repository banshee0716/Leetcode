<h2><a href="https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/">2914. Minimum Number of Changes to Make Binary String Beautiful</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">You are given a <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">0-indexed</strong> binary string <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code> having an even length.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個長度為偶數<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">、索引為 0 的</strong>二進位字串<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code> 。</font></font></font></p>

<p data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">A string is <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">beautiful</strong> if it's possible to partition it into one or more substrings such that:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果可以將字串分成一個或多個子字串，那麼該字串就是<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">美麗的</strong>：</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">Each substring has an <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">even length</strong>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">每個子串的<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">長度均為偶數</strong>。</font></font></font></li>
	<li data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">Each substring contains <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">only</strong> <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">1</code>'s or <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">only</strong> <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">0</code>'s.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">每個子字串<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">僅</strong>包含<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">1</code>或<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">僅包含</strong><code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">0</code> 。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">You can change any character in <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code> to <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">0</code> or <code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">1</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您可以將<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code>中的任何字元變更為<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">0</code>或<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">1</code> 。</font></font></font></p>

<p data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">the <strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">minimum</strong> number of changes required to make the string </em><code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code> <em data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">beautiful</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回使<code data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">s</code>變得<em data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">漂亮</em><em data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">所需的<strong data-immersive-translate-walked="76586049-f568-4e73-83fd-fdc1bc29121c">最少</strong>更改次數</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "1001"
<strong>Output:</strong> 2
<strong>Explanation:</strong> We change s[1] to 1 and s[3] to 0 to get string "1100".
It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "10"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We change s[1] to 1 to get string "11".
It can be seen that the string "11" is beautiful because we can partition it into "11".
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> 0
<strong>Explanation:</strong> We don't need to make any changes as the string "0000" is beautiful already.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> has an even length.</li>
	<li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>
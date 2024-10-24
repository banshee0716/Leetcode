<h2><a href="https://leetcode.com/problems/longest-happy-string/">1405. Longest Happy String</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1">A string <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code> is called <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">happy</strong> if it satisfies the following conditions:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果字串<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code>滿足以下條件，則稱為<strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">happy</strong> ：</font></font></font></p>

<ul>
	<li><code>s</code> only contains the letters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code>.</li>
	<li data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code> does not contain any of <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"aaa"</code>, <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"bbb"</code>, or <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"ccc"</code> as a substring.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code>不包含任何<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"aaa"</code> 、 <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"bbb"</code>或<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">"ccc"</code>作為子字串。</font></font></font></li>
	<li data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code> contains <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">at most</strong> <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">a</code> occurrences of the letter <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'a'</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code><strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">至多</strong>包含字母<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'a'</code> <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">a</code> 。</font></font></font></li>
	<li data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code> contains <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">at most</strong> <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">b</code> occurrences of the letter <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'b'</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code><strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">最多</strong>包含<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">b</code>次出現的字母<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'b'</code> 。</font></font></font></li>
	<li data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code> contains <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">at most</strong> <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">c</code> occurrences of the letter <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'c'</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">s</code><strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">最多</strong>包含<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">c</code>出現的字母<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">'c'</code> 。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1">Given three integers <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">a</code>, <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">b</code>, and <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">c</code>, return <em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">the <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">longest possible happy </strong>string</em>. If there are multiple longest happy strings, return <em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">any of them</em>. If there is no such string, return <em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">the empty string </em><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">""</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定三個整數<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">a</code> 、 <code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">b</code>和<code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">c</code> ，傳回<em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf"><strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">最長的可能快樂</strong>字串</em>。如果有多個最長的快樂字串，則傳回<em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">其中任何一個</em>。如果沒有這樣的字串，則傳回<em data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">空字串</em><code data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">""</code> 。</font></font></font></p>

<p data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">substring</strong> is a contiguous sequence of characters within a string.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="12125c6c-7181-475d-81fd-0684d0c6c5bf">子字串</strong>是字串中連續的字元序列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> a = 1, b = 1, c = 7
<strong>Output:</strong> "ccaccbcc"
<strong>Explanation:</strong> "ccbccacc" would also be a correct answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> a = 7, b = 1, c = 0
<strong>Output:</strong> "aabaa"
<strong>Explanation:</strong> It is the only correct answer in this case.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= a, b, c &lt;= 100</code></li>
	<li><code>a + b + c &gt; 0</code></li>
</ul>
</div>
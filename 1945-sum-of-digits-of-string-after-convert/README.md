<h2><a href="https://leetcode.com/problems/sum-of-digits-of-string-after-convert/">1945. Sum of Digits of String After Convert</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272" data-immersive-translate-paragraph="1">You are given a string <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s</code> consisting of lowercase English letters, and an integer <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個由小寫英文字母組成的字串<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s</code>和一個整數<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k</code> 。</font></font></font></p>

<p data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272" data-immersive-translate-paragraph="1">First, <strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">convert</strong> <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s</code> into an integer by replacing each letter with its position in the alphabet (i.e., replace <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'a'</code> with <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">1</code>, <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'b'</code> with <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">2</code>, ..., <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'z'</code> with <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">26</code>). Then, <strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">transform</strong> the integer by replacing it with the <strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">sum of its digits</strong>. Repeat the <strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">transform</strong> operation <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k</code><strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272"> times</strong> in total.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">首先，透過將每個字母替換為其在字母表中的位置（即，將<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'a'</code>替換為<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">1</code> ，將<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'b'</code>替換為<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">2</code> ，...， <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">'z'</code>替換為<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">26</code> ），將<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s</code><strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">轉換</strong>為整數。然後，透過將其替換<strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">為其數字</strong>總和來<strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">轉換</strong>該整數。總共重複<strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">變換</strong>操作<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k</code><strong data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">次</strong>。</font></font></font></p>

<p data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272" data-immersive-translate-paragraph="1">For example, if <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s = "zbax"</code> and <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k = 2</code>, then the resulting integer would be <code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">8</code> by the following operations:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">例如，如果<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">s = "zbax"</code>且<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">k = 2</code> ，則透過以下操作得到的整數將為<code data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">8</code> ：</font></font></font></p>

<ul>
	<li><strong>Convert</strong>: <code>"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124</code></li>
	<li><strong>Transform #1</strong>: <code>262124 ➝ 2 + 6 + 2 + 1 + 2 + 4&nbsp;➝ 17</code></li>
	<li><strong>Transform #2</strong>: <code>17 ➝ 1 + 7 ➝ 8</code></li>
</ul>

<p data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">the resulting integer after performing the operations described above</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><em data-immersive-translate-walked="c46ddd8f-756d-4131-a8af-0e5ea2966272">執行上述操作後傳回結果整數</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "iiii", k = 1
<strong>Output:</strong> 36
<strong>Explanation:</strong> The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "leetcode", k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "zbax", k = 2
<strong>Output:</strong> 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
</div>
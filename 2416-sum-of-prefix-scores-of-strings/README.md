<h2><a href="https://leetcode.com/problems/sum-of-prefix-scores-of-strings/">2416. Sum of Prefix Scores of Strings</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556" data-immersive-translate-paragraph="1">You are given an array <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words</code> of size <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">n</code> consisting of <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">non-empty</strong> strings.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個大小為<code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">n</code>的<code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words</code>數組，其中包含<strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">非空</strong>字串。</font></font></font></p>

<p data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556" data-immersive-translate-paragraph="1">We define the <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">score</strong> of a string <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">word</code> as the <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">number</strong> of strings <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code> such that <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">word</code> is a <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">prefix</strong> of <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">我們定義一個字串的分數 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">word</code> 作為字串的數量 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code> 這樣 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">word</code> 是一個前綴 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code> 。</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556" data-immersive-translate-paragraph="1">For example, if <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words = ["a", "ab", "abc", "cab"]</code>, then the score of <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> is <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">2</code>, since <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> is a prefix of both <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> and <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"abc"</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">例如，如果 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words = ["a", "ab", "abc", "cab"]</code> ，那麼得分為 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> 是 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">2</code> ， 自從 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> 是兩者的前綴 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"ab"</code> 和 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">"abc"</code> 。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">an array </em><code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">answer</code><em data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556"> of size </em><code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">n</code><em data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556"> where </em><code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">answer[i]</code><em data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556"> is the <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">sum</strong> of scores of every <strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">non-empty</strong> prefix of </em><code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回一個數組 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">answer</code> 尺寸的 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">n</code> 在哪裡 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">answer[i]</code> 是每個非空前綴的分數總和 <code data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">words[i]</code> 。</font></font></font></p>

<p data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556" data-immersive-translate-paragraph="1"><strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">Note</strong> that a string is considered as a prefix of itself.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="d7529878-3ef5-4e4a-a27c-c0f3e16e9556">請注意</strong>，字串被視為其自身的前綴。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["abc","ab","bc","b"]
<strong>Output:</strong> [5,4,3,2]
<strong>Explanation:</strong> The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["abcd"]
<strong>Output:</strong> [4]
<strong>Explanation:</strong>
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
</div>
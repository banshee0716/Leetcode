<h2><a href="https://leetcode.com/problems/delete-characters-to-make-fancy-string/">1957. Delete Characters to Make Fancy String</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db" data-immersive-translate-paragraph="1">A <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">fancy string</strong> is a string where no <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">three</strong> <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">consecutive</strong> characters are equal.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">奇特字串</strong>是指沒有<strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">三個</strong><strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">連續</strong>字元相等的字串。</font></font></font></p>

<p data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db" data-immersive-translate-paragraph="1">Given a string <code data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">s</code>, delete the <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">minimum</strong> possible number of characters from <code data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">s</code> to make it <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">fancy</strong>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個字串<code data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">s</code> ，從<code data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">s</code>中刪除盡可能<strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">少</strong>的字元以使其變得<strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">更漂亮</strong>。</font></font></font></p>

<p data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">the final string after the deletion</em>. It can be shown that the answer will always be <strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">unique</strong>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">刪除後的最終字串</em>。可以證明，答案永遠是<strong data-immersive-translate-walked="47a1e6d1-e49e-4535-aad8-ac110514d2db">唯一的</strong>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "le<u>e</u>etcode"
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong>
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "<u>a</u>aab<u>aa</u>aa"
<strong>Output:</strong> "aabaa"
<strong>Explanation:</strong>
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> "aab"
<strong>Explanation:</strong> No three consecutive characters are equal, so return "aab".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>
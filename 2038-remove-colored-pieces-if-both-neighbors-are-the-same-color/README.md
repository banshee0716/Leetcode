<h2><a href="https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/">2038. Remove Colored Pieces if Both Neighbors are the Same Color</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">There are <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">n</code> pieces arranged in a line, and each piece is colored either by <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> or by <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code>. You are given a string <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">colors</code> of length <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">n</code> where <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">colors[i]</code> is the color of the <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">i<sup>th</sup></code> piece.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">有些 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">n</code> 片段排列成一條線，每件作品的顏色要麼由 或 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> . <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code> 你會得到一個長度的字串 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">colors</code> ，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">colors[i]</code> 是 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">i<sup>th</sup></code> 作品 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">n</code> 的顏色。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">Alice and Bob are playing a game where they take <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">alternating turns</strong> removing pieces from the line. In this game, Alice moves<strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f"> first</strong>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">愛麗絲和鮑勃正在玩一個遊戲，他們輪流從線上移除碎片。在這個遊戲中，愛麗絲首先移動。</font></font></font></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">Alice is only allowed to remove a piece colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> if <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">both its neighbors</strong> are also colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code>. She is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">not allowed</strong> to remove pieces that are colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">僅當兩個相鄰的碎片也都著色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> 時，才允許愛麗絲刪除彩色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> 的碎片。她不允許刪除有色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code> 的碎片。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">Bob is only allowed to remove a piece colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code> if <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">both its neighbors</strong> are also colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code>. He is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">not allowed</strong> to remove pieces that are colored <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">僅當兩個相鄰的塊也都著色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code> 時，才允許鮑勃刪除著色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'B'</code> 的碎片。他不允許刪除有色 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">'A'</code> 的碎片.</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">Alice and Bob <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">cannot</strong> remove pieces from the edge of the line.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">愛麗絲和鮑勃無法從線的邊緣移除碎片。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">If a player cannot make a move on their turn, that player <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">loses</strong> and the other player <strong data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">wins</strong>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果一個玩家在回合不能採取行動，則該玩家輸了，而另一個玩家獲勝。</font></font></font></li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">Assuming Alice and Bob play optimally, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">true</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f"> if Alice wins, or return </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">false</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f"> if Bob wins</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">假設愛麗絲和鮑勃玩得最佳，如果愛麗絲贏了，就返回，或者如果鮑勃贏了，就返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">true</code>  <code data-immersive-translate-effect="1" data-immersive_translate_walked="bd67edcc-0bd6-4029-a1dd-4fbfb2c1a68f">false</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> colors = "AAABABB"
<strong>Output:</strong> true
<strong>Explanation:</strong>
A<u>A</u>ABABB -&gt; AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> colors = "AA"
<strong>Output:</strong> false
<strong>Explanation:</strong>
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> colors = "ABBBBBBBAAA"
<strong>Output:</strong> false
<strong>Explanation:</strong>
ABBBBBBBA<u>A</u>A -&gt; ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBB<u>B</u>BBAA -&gt; ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;colors.length &lt;= 10<sup>5</sup></code></li>
	<li><code>colors</code>&nbsp;consists of only the letters&nbsp;<code>'A'</code>&nbsp;and&nbsp;<code>'B'</code></li>
</ul>
</div>
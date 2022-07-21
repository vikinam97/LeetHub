<div class="pusher"><div><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Form a palindrome<i aria-hidden="true" class="bookmark outline large icon"></i></h3></div><i aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span class="problems_green__cbqrD"><strong>Medium</strong></span><span>Accuracy: <strong>53.0%</strong></span><span>Submissions: <strong>27493</strong></span><span>Points: <strong>4</strong></span></div><div class="ui divider"></div><div><div><a href="https://practice.geeksforgeeks.org/explore?page=1&amp;curated[]=1&amp;sortBy=submissions" target="_blank"><div style="margin: 14px 0px !important;" class="row"><div class="col-md-12 problems-promotional_banner" style="cursor:pointer; background: #EFF8F3 0% 0% no-repeat padding-box; display: flex; align-items: center; position:                     relative; padding: 1.5%; border-radius: 10px; justify-content: center; text-align: center; font-weight: 600; color: #333;                     font-size: 16px; font-family: sofia-pro"> <img src="https://media.geeksforgeeks.org/img-practice/MaskGroup72-1652267405.svg" alt="Lamp" width="46" height="40" style="background: transparent 0% 0% no-repeat padding-box;opacity: 1; margin: 0 16px;"> <div style="display: flex;"> <span> This problem is part of GFG SDE Sheet. Click here to view more. &nbsp; </span>                             <img src="https://media.geeksforgeeks.org/img-practice/external-1657081738.svg"></div>                         </div></div></a></div><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string, find the minimum number of characters to be inserted to convert it to palindrome.<br>
For Example:<br>
ab: Number of insertions required is 1.&nbsp;<strong>b</strong>ab or aba<br>
aa: Number of insertions required is 0. aa<br>
abcd: Number of insertions required is 3.&nbsp;<strong>dcb</strong>abcd</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> str = "abcd"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Inserted character marked
with bold characters in <strong>dcb</strong>abcd
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> str = "aa"
<strong>Output:</strong> 0
<strong>Explanation:</strong>"aa" is already a palindrome.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>countMin()</strong>&nbsp;which takes the string <strong>str&nbsp;</strong>as inputs and returns the answer.<br>
<br>
<strong>Expected Time Complexity:</strong>&nbsp;O(N<sup>2</sup>), N = |str|<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N<sup>2</sup>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ |str|&nbsp;≤ 10<sup>3</sup><br>
str contains only lower case alphabets.</span></p>
</div></div></div></div>
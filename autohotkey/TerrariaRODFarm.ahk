#SingleInstance force
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


#maxThreadsPerHotkey, 2
;setKeyDelay, 50, 50 ;; TODO: MAYBE USE THIS
;setMouseDelay, 50

MouseToTop() ;; TODO: maybe turn into MoveMouse func, with variable to determine where to (preset locations)
{
	; Move mouse to center, top quarter of screen
	CoordMode, Mouse, Screen
	MouseMove, A_ScreenWidth/2, A_ScreenHeight/4
}

MouseToLeft()
{
	; Move mouse to center, top quarter of screen
	CoordMode, Mouse, Screen
	MouseMove, A_ScreenWidth/4, A_ScreenHeight/2
}

MouseToRight()
{
	; Move mouse to center, top quarter of screen
	CoordMode, Mouse, Screen
	MouseMove, A_ScreenWidth - A_ScreenWidth/4, A_ScreenHeight/2
}

MouseToBottom()
{
	; Move mouse to center, top quarter of screen
	CoordMode, Mouse, Screen
	MouseMove, A_ScreenWidth/2, A_ScreenHeight - A_ScreenHeight/4
}

Fire()
{
	; Click
	Click, down, left
	Sleep, 50
	Click, up, left
}

ChangeItem(ItemNum)
{
	Send {%ItemNum% down}
	Sleep, 50
	Send {%ItemNum% up}
}


active:=0
i:=0

sunfury:=0
sunfuryFreq:=25

summon:=1
summonFreq:=150

Gui, Color, White

Gui, -caption +toolwindow +AlwaysOnTop

Gui, font, s30 bold, Arial

Gui, add, text, vTX cRed TransColor, %i%

Gui, Show, % "x" A_ScreenWidth-300 " y" A_ScreenHeight-130 ,TRANS-WIN

WinSet, TransColor, White, TRANS-WIN


$f1::
	active:=!active
	
	if (active = 1) 
	{
		i:=0
		GuiControl, Show, TX
	} 
	else
	{
		GuiControl, Hide, TX
	}

	while (active=1)
	{
		Loop 4 {
			Send {Space down}
			Sleep, 150
			Send {Space up}
			
			Sleep, 150
		}
		;; Fire Crystal Vile Shard ;;
		; Change weapon to #5
		ChangeItem(5)
		
		; Move mouse to center, top quarter of screen
		MouseToTop()
		
		; Click
		Fire()
		
		;; Activates every 100 cycles, including first
		if ( Mod(i, summonFreq) = 0)
		{
			; Change weapon to #0
			ChangeItem(0)

			; Move mouse to center, top quarter of screen
			MouseToTop()
			
			Sleep, 500

			; Click
			Fire()

			Sleep, 150
		}

		;; Activates every 25 cycles, including first. Sunfury protect
		if ( Mod(i, sunfuryFreq) = 0 AND sunfury == 1)
		{
			ChangeItem(4) ;Sunfury

			MouseToLeft()
			Sleep, 500
			Fire()

			Sleep, 150

			MouseToRight()
			Sleep, 500
			Fire()

			Sleep, 150

			MouseToBottom()
			Sleep, 500
			Fire()

			Sleep, 150
		}

		i++
		GuiControl, Text, TX, %i%

		Sleep, 150
	}
return

^End::
	ExitApp
return
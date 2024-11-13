class nokia_switches:
	def __init__(self):
		self.menu_caller = NokiaMenus()
		self.phonebook_answer = 0
		self.messages_answer = 0
		self.message_settings_answer = 0
		self.call_register_answer = 0
		self.settings_answer = 0
		self.tones_answer = 0
		self.clock_answer = 0
		self.menu_answer = 0

	def main_menu_switch(self, menu_answer) {
		self.menu_caller = NokiaMenus()
		self.phonebook_answer = 0
		self.messages_answer = 0
		self.message_settings_answer = 0
		self.call_register_answer = 0
		self.settings_answer = 0
		self.tones_answer = 0
		self.clock_answer = 0
		self.menu_answer = 0

		if menu_answer == 0:
			menu_answer = int(input(self.menu_caller.main_menu))
			self.main_menu.switch(menu_answer)

		elif menu_answer == 1:
			phonebook_answer = int(input(self.menu_caller.phonebook_menu))
			self.phonebook_switch(phonebook_answer)

		elif menu_answer == 2:
			messages_answer = int(input(self.menu_caller.messages_menu))
			self.messages_switch(messages_answer)

		elif menu_answer == 3:
			print(self.menu_caller.chat_menu)

		elif menu_answer == 4:
			call_register_answer = int(input(self.menu_caller.call_register_menu))
			self.call_register_switch(call_register_answer)

		elif menu_answer == 5:
			self.tones_answer = int(input(self.menu_caller.tones_menu))
			self.tones_switch(tones_answer)

		elif menu_answer == 6:
			settingsAnswer = int(input(self.menu_caller.settings_menu))
			self.settings_switch(settings_answer)

		elif menu_answer == 7:
			print(self.menu_caller.call_divert_menu)

		elif menu_answer == 8:
			print(self.menu_caller.games_menu)

		elif menu_answer == 9:
			print(self.menu_caller.games_menu)

		elif menu_answer == 10:
			print(self.menu_caller.calculator_menu)

		elif menu_answer == 11:
			clock_answer = int(input(self.menu_caller.clock_menu))
			self.clock_switch(clock_answer)

		elif menu_answer == 12:
			print(self.menu_caller.profiles_menu)

		elif menu_answer == 13:
			print(self.menu_caller.sim_services_menu)

		elif menu_answer == 14:
			print(self.menu_caller.power_off)

		else:
			print("\nInvalid input\n")


	public void phoneBookSwitch(int phoneBookAnswer) {

		if (phoneBookAnswer == 11 | returnToPhoneBook) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (phoneBookAnswer) {

			case 1: System.out.println("\nSearch\n"); break;
			case 2: System.out.println("\nService Nos.\n"); break;
			case 3: System.out.println("\nAdd name\n"); break;
			case 4: System.out.println("\nErase\n"); break;
			case 5: System.out.println("\nEdit\n"); break;
			case 6: System.out.println("\nAssign tone\n"); break;
			case 7: System.out.println("\nSend b'card\n"); break;
			case 8: System.out.println(menuCaller.optionsMenu);
				int optionsAnswer = input.nextInt();
				optionsSwitch(optionsAnswer);
				break;
			
			case 9: System.out.println("\nSpeed dials\n"); break;
			case 10: System.out.println("\nVoice\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void optionsSwitch(int optionsAnswer) {

		if (optionsAnswer == 3) {
		mainMenuSwitch(1);
		return;
		}
		else {

		switch (optionsAnswer) {

			case 1: System.out.println("\nType of view\n"); break;
			case 2: System.out.println("\nMemory status\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void messagesSwitch(int messagesAnswer) {

		if (messagesAnswer == 11) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (messagesAnswer) {

			case 1: System.out.println("\nWrite messages\n"); break;
			case 2: System.out.println("\nInbox\n"); break;
			case 3: System.out.println("\nOutbox\n"); break;
			case 4: System.out.println("\nPicture messages\n"); break;
			case 5: System.out.println("\nTemplates\n"); break;
			case 6: System.out.println("\nSmileys\n"); break;
			case 7: System.out.println(menuCaller.messageSettingsMenu);
				int messageSettingsAnswer = input.nextInt();
				messageSettingsSwitch(messageSettingsAnswer);
				break;

			case 8: System.out.println("\nInfo service\n"); break;
			case 9: System.out.println("\nVoice mailbox number\n"); break;
			case 10: System.out.println("\nService command editor\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void messageSettingsSwitch(int messageSettingsAnswer) {

		if (messageSettingsAnswer == 3) {
		mainMenuSwitch(2);
		return;
		}
		else {

		switch (messageSettingsAnswer) {

			case 1: System.out.print(menuCaller.setOneMenu);
				int setOneAnswer = input.nextInt();
				setOneSwitch(setOneAnswer);
				break;

			case 2: System.out.print(menuCaller.commonMenu);
				int commonAnswer = input.nextInt();
				commonSwitch(commonAnswer);
				break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void setOneSwitch(int setOneAnswer) {

		if (setOneAnswer == 4) {
		mainMenuSwitch(2);
		return;
		}
		else {

		switch (setOneAnswer) {

			case 1: System.out.println("\nMessage centre number\n"); break;
			case 2: System.out.println("\nMessages sent as\n"); break; 
			case 3: System.out.println("\nMessage validity\n"); break; 
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void commonSwitch(int commonAnswer) {

		if (commonAnswer == 4) {
		mainMenuSwitch(2);
		return;
		}
		else {

		switch (commonAnswer) {

			case 1: System.out.println("\nDelivery reports\n"); break;
			case 2: System.out.println("\nReply via same centre\n"); break; 
			case 3: System.out.println("\nCharacter support\n"); break; 
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void callRegisterSwitch(int callRegisterAnswer) {

		if (callRegisterAnswer == 9) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (callRegisterAnswer) { 

			case 1: System.out.println("\nMissed calls\n"); break;
			case 2: System.out.println("\nReceived calls\n"); break;
			case 3: System.out.println("\nDialled numbers\n"); break;
			case 4: System.out.println("\nErase recent call lists\n"); break;
			case 5: System.out.print(menuCaller.showCallDurationMenu);
				int showCallDurationAnswer = input.nextInt();
				showCallDurationSwitch(showCallDurationAnswer);
				break;

			case 6: System.out.print(menuCaller.showCallCostsMenu);
				int showCallCostsAnswer = input.nextInt();
				showCallCostsSwitch(showCallCostsAnswer);
				break;

			case 7: System.out.print(menuCaller.callCostSettingsMenu);
				int callCostSettingsAnswer = input.nextInt();
				callCostSettingsSwitch(callCostSettingsAnswer);
				break;

			case 8: System.out.println("\nPrepaid credit\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void showCallDurationSwitch(int showCallDurationAnswer) {

		if (showCallDurationAnswer == 6) {
		mainMenuSwitch(4);
		return;
		}
		else {

		switch (showCallDurationAnswer) {

			case 1: System.out.print("\nLast call duration\n"); break;
			case 2: System.out.print("\nAll calls' duration\n"); break;
			case 3: System.out.print("\nReceived call's duration\n"); break;
			case 4: System.out.print("\nDialled calls' duration\n"); break;
			case 5: System.out.print("\nTimers cleared\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void showCallCostsSwitch(int showCallCostsAnswer) {

		if (showCallCostsAnswer == 4) {
		mainMenuSwitch(4);
		return;
		}
		else {

		switch (showCallCostsAnswer) {

			case 1: System.out.print("\nLast call cost\n"); break;
			case 2: System.out.print("\nAll calls' cost\n"); break;
			case 3: System.out.print("\nCounters cleared\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void callCostSettingsSwitch(int callCostSettingsAnswer) {

		if (callCostSettingsAnswer == 3) {
		mainMenuSwitch(4);
		return;
		}
		else {

		switch (callCostSettingsAnswer) {

			case 1: System.out.print("\nCall cost settings\n"); break;
			case 2: System.out.print("\nShow costs in\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void tonesSwitch(int tonesAnswer) {

		if (tonesAnswer == 10) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (tonesAnswer) {

			case 1: System.out.println("\nRinging tone\n"); break;
			case 2: System.out.println("\nRinging volume\n"); break;
			case 3: System.out.println("\nIncoming call alert\n"); break;
			case 4: System.out.println("\nComposer\n"); break;
			case 5: System.out.println("\nMessage alert tone\n"); break;
			case 6: System.out.println("\nKeypad tones\n"); break;
			case 7: System.out.println("\nWarning and game tone\n"); break;
			case 8: System.out.println("\nVibrating alert\n"); break;
			case 9: System.out.println("\nScreen saver\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void settingsSwitch(int settingsAnswer) {

		if (settingsAnswer == 5) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (settingsAnswer) {

			case 1: System.out.println(menuCaller.callSettingsMenu);
				int callSettingsAnswer = input.nextInt();
				callSettingsSwitch(callSettingsAnswer);
				break;

			case 2: System.out.print(menuCaller.phoneSettingsMenu);
				int phoneSettingsAnswer = input.nextInt();
				phoneSettingsSwitch(phoneSettingsAnswer);
				break;

			case 3: System.out.println(menuCaller.securitySettingsMenu);
				int securitySettingsAnswer = input.nextInt();
				securitySettingsSwitch(securitySettingsAnswer);
				break;

			case 4: System.out.println("\nRestore factory settings\n"); break;
			default: System.out.print("\nInvalid input\n"); break;

		}

		}

	}

	public void callSettingsSwitch(int callSettingsAnswer) {

		if (callSettingsAnswer == 7) {
		mainMenuSwitch(6);
		return;
		}
		else {

		switch (callSettingsAnswer) {

			case 1: System.out.println("\nAutomatic redial\n"); break;
			case 2: System.out.println("\nSpeed dialling\n"); break;
			case 3: System.out.println("\nCall waiting options\n"); break;
			case 4: System.out.println("\nOwn number sending\n"); break;
			case 5: System.out.println("\nPhone line in use\n"); break;
			case 6: System.out.println("\nAutomatic answer\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void phoneSettingsSwitch(int phoneSettingsAnswer) {

		if (phoneSettingsAnswer == 7) {
		mainMenuSwitch(6);
		return;
		}
		else {

		switch (phoneSettingsAnswer) {

			case 1: System.out.println("\nLanguage\n"); break;
			case 2: System.out.println("\nCell info display\n"); break;
			case 3: System.out.println("\nWelcome note\n"); break;
			case 4: System.out.println("\nNetwork selection\n"); break;
			case 5: System.out.println("\nLights\n"); break;
			case 6: System.out.println("\nConfirm SIM service actions\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void securitySettingsSwitch(int securitySettingsAnswer) {

		if (securitySettingsAnswer == 7) {
		mainMenuSwitch(6);
		return;
		}
		else {

		switch (securitySettingsAnswer) {

			case 1: System.out.println("\nPIN code request\n"); break;
			case 2: System.out.println("\nCall barring service\n"); break;
			case 3: System.out.println("\nFixed dialling\n"); break;
			case 4: System.out.println("\nClosed user group\n"); break;
			case 5: System.out.println("\nPhone security\n"); break;
			case 6: System.out.println("\nChange access codes\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

	public void clockSwitch(int clockAnswer) {

		if (clockAnswer == 7) {
		mainMenuSwitch(0);
		return;
		}
		else {

		switch (clockAnswer) {

			case 1: System.out.println("\nAlarm clock\n"); break;
			case 2: System.out.println("\nClock settings\n"); break;
			case 3: System.out.println("\nDate setting\n"); break;
			case 4: System.out.println("\nStopwatch\n"); break;
			case 5: System.out.println("\nCountdown timer\n"); break;
			case 6: System.out.println("\nAuto update of date and time\n"); break;
			default: System.out.println("\nInvalid input\n"); break;

		}

		}

	}

}

































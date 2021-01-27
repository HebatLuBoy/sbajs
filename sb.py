#Creator : HebatLuBot .Corp
#Team : HebatLuBoy™
#Version : SELFBOT ONLY + ANTI-JS
from PEOPLE.WEAREYOUTEAM import *
from PEOPLE.akad.ttypes import Message
from PEOPLE.akad.ttypes import ContentType as Type
from threading import Thread
from datetime import datetime
from datetime import timedelta, date
from time import sleep
import time, random, multiprocessing, sys, json, codecs, threading, traceback, glob, re, string, asyncio, os, requests, subprocess, six, urllib, urllib.parse
import time, random, pytz, atexit, ctypes, livejson, sys, shutil, json, codecs, ast, threading, glob, re, string, asyncio, os, traceback, requests, six, unicodedata, subprocess, signal
XeberlhynWaktu = time.time()

#XeberlhynBoss = LINE("TAROK TOKEN UTAMA SB DISINI",appName="IOS\t10.1.1\tiOS\t13.3.1")
#XeberlhynAJS = LINE("TAROK TOKEN ANTIJS DISINI",appName="IOS\t10.1.1\tiOS\t13.3.1")


XeberlhynBoss = LINE("emailpunyalu@gmail.com"."passwordnya")
XeberlhynAJS = LINE("emailpunyalu@gmail.com"."passwordnya")

print ("= SelfBot Antijs Succes Login =")
MyCreatorXeberlhyn = OEPoll(XeberlhynBoss)
call = XeberlhynBoss
People = XeberlhynBoss.getProfile().mid
Berlin = XeberlhynAJS.getProfile().mid
Pasukan =[People,Berlin]
Creators = ["u7c12144cc680c22acfd886ed81908b75"]
President = "u7c12144cc680c22acfd886ed81908b75"
JandaBahenol = []
Bangsat = {
    "Daftarhitam": {},
    "link": {},
    "kickers": {},
    "Algojo": {
        "u7c12144cc680c22acfd886ed81908b75": True
    },
    "paraundangan": {},
    "JeritanJanda": {},
    "SelfiPakeHandiCam": False
}
WhatTheFuck = Pasukan + Creators
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def BergerakTanpaBtasBosKu():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def BerlinLoveRieny(TeamPeopleBoTS):
    global time
    global ast
    global groupParam
    try:
        if TeamPeopleBoTS.type == 0:
            return
        if TeamPeopleBoTS.type == 13:
            if People in TeamPeopleBoTS.param3:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    XeberlhynBoss.acceptGroupInvitation(TeamPeopleBoTS.param1)
                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"ꜱᴏʀʀʏ, ʟᴜ ʙᴜᴋᴀɴ ʙᴏꜱ ɢᴜᴀ ᴀɴᴊɪɴɢ!")
                    XeberlhynBoss.leaveGroup(TeamPeopleBoTS.param1)
                else:
                    XeberlhynBoss.acceptGroupInvitation(TeamPeopleBoTS.param1)
                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"ᴍɪꜱɪ, ɴᴜᴍᴘᴀɴɢ ᴏᴘᴇɴ ʙᴏ !!!")
            if TeamPeopleBoTS.param2 in Bangsat["Daftarhitam"]:
                if TeamPeopleBoTS.param2 in Creators and TeamPeopleBoTS.param2 in Pasukan and TeamPeopleBoTS.param2 in Bangsat["Algojo"]:
                    pass
                else:
                    try:
                        BangsatTerhormat = XeberlhynBoss.getCompactGroup(TeamPeopleBoTS.param1)
                        if BangsatTerhormat.invitee is not None:
                            FuckyouMan = [a.mid for a in BangsatTerhormat.invitee]
                            for MakhlukJahanam in FuckyouMan:
                                if MakhlukJahanam in TeamPeopleBoTS.param3:
                                    XeberlhynBoss.cancelGroupInvitation(TeamPeopleBoTS.param1, [MakhlukJahanam])
                                    XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1, [MakhlukJahanam])
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1, [TeamPeopleBoTS.param2])
                    except:
                        pass
            if TeamPeopleBoTS.param3 in Bangsat["Daftarhitam"]:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                    try:
                        XeberlhynBoss.cancelGroupInvitation(TeamPeopleBoTS.param1, [TeamPeopleBoTS.param3])
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1, [TeamPeopleBoTS.param2])
                    except:
                        pass                    
        if TeamPeopleBoTS.type == 13:
            if TeamPeopleBoTS.param1 in Bangsat["JeritanJanda"]:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    try:
                        BrutalKelasDewa = Xeberlhyn.getCompactGroup(TeamPeopleBoTS.param1)
                        if BrutalKelasDewa.invitee is not None:
                           Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                           FuckyouMan = [a.mid for a in BrutalKelasDewa.invitee]
                           for MakhlukBiadap in FuckyouMan:
                               if MakhlukBiadap in TeamPeopleBoTS.param3:
                                  Bangsat["Daftarhitam"][MakhlukBiadap] = True
                                  XeberlhynBoss.cancelGroupInvitation(TeamPeopleBoTS.param1,[MakhlukBiadap])
                                  XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1, [MakhlukBiadap])
                           XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                    except:pass
        if TeamPeopleBoTS.type == 17:
            if TeamPeopleBoTS.param2 in Bangsat["Daftarhitam"]:
                XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
        if TeamPeopleBoTS.type == 11:
            if TeamPeopleBoTS.param1 in Bangsat["link"]:
                if XeberlhynBoss.getGroup(TeamPeopleBoTS.param1).preventedJoinByTicket == False:
                    if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                        X = XeberlhynBoss.getGroup(TeamPeopleBoTS.param1)
                        X.preventedJoinByTicket = True
                        Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                        Z = XeberlhynBoss.getGroup(TeamPeopleBoTS.param1)
                        Z.preventedJoinByTicket = True
                        XeberlhynBoss.updateGroup(Z)
        if TeamPeopleBoTS.type == 11:
            if TeamPeopleBoTS.param2 in Bangsat["Daftarhitam"]:
                try:
                    if XeberlhynBoss.getGroup(TeamPeopleBoTS.param1).preventedJoinByTicket == False:
                        if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                            XeberlhynBoss.reissueGroupTicket(TeamPeopleBoTS.param1)
                            X = XeberlhynBoss.getGroup(TeamPeopleBoTS.param1)
                            X.preventedJoinByTicket = True
                            XeberlhynBoss.updateGroup(X)
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                except:
                    pass
        if TeamPeopleBoTS.type == 19 or TeamPeopleBoTS.type == 32:
            try:
                if TeamPeopleBoTS.param1 in JandaBahenol:
                    if TeamPeopleBoTS.param3 in People:
                        if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                            Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                            XeberlhynAJS.acceptGroupInvitation(TeamPeopleBoTS.param1)
                            G = XeberlhynAJS.getGroup(TeamPeopleBoTS.param1)
                            G.preventedJoinByTicket = False
                            XeberlhynAJS.updateGroup(G)
                            invsend = 0
                            SuratPanggilan = XeberlhynAJS.reissueGroupTicket(TeamPeopleBoTS.param1)
                            XeberlhynBoss.acceptGroupInvitationByTicket(TeamPeopleBoTS.param1,SuratPanggilan)
                            XeberlhynAJS.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            G.preventedJoinByTicket = True
                            XeberlhynAJS.updateGroup(G)
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            XeberlhynAJS.leaveGroup(TeamPeopleBoTS.param1)
                            XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[Berlin])
                            XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"⌬ AntiJS telah di invite ulang")
                        else:
                           pass
                if TeamPeopleBoTS.param3 in Berlin:
                    if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                        Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                        XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[Berlin])
                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"• Goblog , AntiJS di cancel")
                    else:
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                        XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[Berlin])
                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"• Goblog , AntiJS di cancel")
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    if TeamPeopleBoTS.param3 in Creators:
                        if TeamPeopleBoTS.param1 in JandaBahenol:
                            Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            XeberlhynBoss.findAndAddContactsByMid(TeamPeopleBoTS.param3)
                            XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param3])
                            XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(TeamPeopleBoTS.param1,"• Pengurus Bot Diinvite")
                else:
                    pass
            except:
                pass
        if TeamPeopleBoTS.type == 19:
            try:
                if President in TeamPeopleBoTS.param3:
                    if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                        Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                        XeberlhynBoss.findAndAddContactsByMid(President)
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                        XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[President])
                    else:
                        pass
            except:
                pass             
        if TeamPeopleBoTS.type == 55:
            if TeamPeopleBoTS.param2 in Bangsat["Daftarhitam"]:
                XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
            else:
                pass
        if TeamPeopleBoTS.type == 25 or TeamPeopleBoTS.type == 26:
            try:
                ShirashiBOTSPeoplE = TeamPeopleBoTS.message
                text = str(ShirashiBOTSPeoplE.text)
                ShirashiBOTSPeoplE_id = ShirashiBOTSPeoplE.id
                ClanSquadters = ShirashiBOTSPeoplE.to
                AreyouReady = ShirashiBOTSPeoplE._from
                if ShirashiBOTSPeoplE.toType == 0 or ShirashiBOTSPeoplE.toType == 1 or ShirashiBOTSPeoplE.toType == 2:
                    if ShirashiBOTSPeoplE.toType == 0:
                        if AreyouReady != XeberlhynBoss.profile.mid:
                            ByCreatorsBerlHyn = AreyouReady
                        else:
                            ByCreatorsBerlHyn = ClanSquadters
                    elif ShirashiBOTSPeoplE.toType == 1:
                        ByCreatorsBerlHyn = ClanSquadters
                    elif ShirashiBOTSPeoplE.toType == 2:
                        ByCreatorsBerlHyn = ClanSquadters
                    if ShirashiBOTSPeoplE.contentType == 0:
                        if text is None:
                            return
                        else:
                            ThePeopleTeamBOTS = text.lower()
                            if ThePeopleTeamBOTS == "restart":
                                if AreyouReady in Creators:
                                    GoyangkanBadanmuShagy = "❖ Bot sukses direset ulang"
                                    contact = XeberlhynBoss.getContact(AreyouReady)
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, GoyangkanBadanmuShagy)
                                    BergerakTanpaBtasBosKu()
                            if ThePeopleTeamBOTS == "xhelp":
                                if AreyouReady in Creators:
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "╭──「 ᴍᴇɴᴜ ꜱᴇʟꜰʙᴏᴛꜱ  」\n│❖ ʀᴇꜱᴛᴀʀᴛ\n│❖ ꜱᴘᴇᴇᴅ\n│❖ .ꜱᴛᴀᴛᴜꜱ\n│❖ ᴄᴇᴋ ᴍᴀɴᴛᴀɴ\n│❖ ʀᴇᴄʜᴀᴛ\n│❖ .ʙʏᴇᴍᴇ\n│❖ ᴄᴇᴋ ᴘᴀᴄᴀʀ\n│❖ ꜱɪɴɪ ᴡᴏɪ\n│❖ ᴘᴜʟᴀɴɢ ɢɪʜ\n│❖ ꜱᴀʏᴀɴɢ(ᴀᴊꜱ ꜱᴛᴀʏ)\n│❖ ꜱʙᴀᴅᴅ: [ᴛᴇʀɢᴇᴛ]\n│❖ ꜱʙᴋɪᴄᴋ: [ᴛᴀʀɢᴇᴛ]\n│❖ ꜱʙɪɴᴠɪᴛᴇ: [ᴛᴀʀɢᴇᴛ]\n│❖ ᴀᴅᴅʙᴏᴛꜱ: [ᴛᴀʀɢᴇᴛ]\n│❖ ᴅᴇʟʟʙᴏᴛꜱ: [ᴛᴇʀɢᴇᴛ]\n│❖ ʙʟᴀᴄᴋʟɪꜱᴛ\n│❖ ᴅᴀꜰᴛᴀʀʙᴏᴛ\n│❖ ᴄʙᴀɴ\n│❖ ꜱʙɢᴀɴᴛɪɴᴀᴍᴀ: [ᴛᴇxᴛ]\n│❖ ᴀᴊꜱɢᴀɴᴛɪɴᴀᴍᴀ: [ᴛᴇxᴛ]\n│❖ ᴜᴘᴅᴀᴛᴇ ᴘɪᴄᴛᴜʀᴇ\n│❖ ᴘʀᴏʀᴇᴄᴛQʀ ᴏɴ/ᴏꜰꜰ\n│❖ ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ/ᴏꜰꜰ\n│❖ ᴘʀᴏᴛᴇᴄᴛɪɴᴠ ᴏɴ/ᴏꜰꜰ\n│❖ ᴘʀᴏʀᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ/ᴏꜰꜰ\n│❖ ᴘʀᴏʀᴇᴄᴛᴀɴᴛɪᴊꜱ ᴏɴ/ᴏꜰꜰ\n╰─────「 グレートユーボーイ 」")
                            if ThePeopleTeamBOTS == ".status":
                                if AreyouReady in Creators:
                                    AnakPerawanBisaDesah = "╭──「 Status SelfBots  」\n"
                                    if ByCreatorsBerlHyn in Bangsat["link"]: AnakPerawanBisaDesah += "│❖ Protectqr on\n"
                                    else: AnakPerawanBisaDesah += "│❖Protectqr off\n"
                                    if ByCreatorsBerlHyn in Bangsat["kickers"]: AnakPerawanBisaDesah += "│❖ Protectkick on\n"
                                    else: AnakPerawanBisaDesah += "│❖Protectkick off\n"
                                    if ByCreatorsBerlHyn in Bangsat["paraundangan"]: AnakPerawanBisaDesah += "│❖ Protectcancel on\n"
                                    else: AnakPerawanBisaDesah += "│❖Protectcancel off\n"
                                    if ByCreatorsBerlHyn in Bangsat["JeritanJanda"]: AnakPerawanBisaDesah += "│❖ Protectinvite on\n"
                                    else: AnakPerawanBisaDesah += "│❖Protectinvite off\n"
                                    if ByCreatorsBerlHyn in JandaBahenol: AnakPerawanBisaDesah += "│❖ Protectantijs on\n"
                                    else: AnakPerawanBisaDesah += "│❖Protectantijs off\n"
                                    AnakPerawanBisaDesah += "╰────「 グレートユーボーイ 」"
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, AnakPerawanBisaDesah)
                            if ThePeopleTeamBOTS == "rechat":
                                if AreyouReady in Creators:
                                    XeberlhynBoss.removeAllMessages(TeamPeopleBoTS.param2)
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Succes menghapus semua pesan」")
                            if ThePeopleTeamBOTS == "sp":
                                if AreyouReady in Creators:
                                    XeberlhynWaktu = time.time()
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "Loading Speed...")
                                    Keputusan = time.time() - XeberlhynWaktu
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "{}".format(str(Keputusan)))
                            if ThePeopleTeamBOTS == ".byeme":
                                if AreyouReady in Creators:
                                    if ShirashiBOTSPeoplE.toType == 2:
                                        try:
                                            XeberlhynBoss.leaveGroup(ByCreatorsBerlHyn)
                                        except:pass
                            if ThePeopleTeamBOTS == "sini woi":
                                if AreyouReady in Creators:
                                    G = XeberlhynBoss.getGroup(ByCreatorsBerlHyn)
                                    ginfo = XeberlhynBoss.getGroup(ByCreatorsBerlHyn)
                                    G.preventedJoinByTicket = False
                                    XeberlhynBoss.updateGroup(G)
                                    invsend = 0
                                    SuratUndangan = XeberlhynBoss.reissueGroupTicket(ByCreatorsBerlHyn)
                                    XeberlhynAJS.acceptGroupInvitationByTicket(ByCreatorsBerlHyn,SuratUndangan)
                                    XeberlhynAJS.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," ᴀᴅᴀ ᴀᴘᴀ ᴛᴜᴀɴ ,ᴘᴀɴɢɢɪʟ ꜱᴀʏᴀ ? ")
                                    G = XeberlhynBoss.getGroup(ByCreatorsBerlHyn)
                                    G.preventedJoinByTicket = True
                                    XeberlhynBoss.updateGroup(G)
                            if ThePeopleTeamBOTS == "pulang gih":
                                if AreyouReady in Creators:
                                    if ShirashiBOTSPeoplE.toType == 2:
                                        try:
                                            XeberlhynAJS.leaveGroup(ByCreatorsBerlHyn)
                                        except:pass
                            if ThePeopleTeamBOTS == "sayang":
                                if AreyouReady in Creators:
                                    XeberlhynBoss.findAndAddContactsByMid(Berlin)
                                    XeberlhynBoss.inviteIntoGroup(ByCreatorsBerlHyn,[Berlin])
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn,"ᴘᴀᴄᴀʀᴀ ᴀɴᴅᴀ ꜱᴜᴅᴀʜ ᴅɪ ᴋᴀᴍᴀʀ, ꜱɪᴀᴘ ᴅɪ ᴇᴋꜱᴇᴋᴜꜱɪ")
                            if ThePeopleTeamBOTS == "cek mantan":
                                if AreyouReady in Creators:
                                    try:XeberlhynBoss.inviteIntoGroup(ByCreatorsBerlHyn, [People]);LonteArab = "OK"
                                    except:LonteArab = "NOT"
                                    if LonteArab == "OK":Terhormat = "ᴀᴋᴜ ꜱɪᴀᴘ ᴅɪ ᴇᴋꜱᴇᴋᴜꜱɪ ʙᴇʙ~"
                                    else:Terhormat = "ɢᴀᴋ ᴅᴜʟᴜ ʟᴀɢɪ ᴘᴍꜱ, ᴄᴏʙᴀ ᴋᴇ ᴘᴀᴄᴀʀ ᴋᴀᴍᴜ~"
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, Terhormat)
                            if ThePeopleTeamBOTS == "cek pacar":
                                if AreyouReady in Creators:
                                    try:XeberlhynAJS.inviteIntoGroup(ByCreatorsBerlHyn, [Berlin]);LonteArab = "OK"
                                    except:LonteArab = "NOT"
                                    if LonteArab == "OK":Terhormat = "ᴇᴋꜱᴇᴋᴜꜱɪ ᴀᴋᴜ ꜱᴀʏᴀɴɢ, ᴀʜ ᴀʜ ᴀʜ~"
                                    else:Terhormat = "ɢᴀᴋ ᴅᴜʟᴜ ʟᴀɢɪ ᴘᴍꜱ, ,ᴄᴏʙᴀ ᴋᴇ ᴍᴀɴᴛᴀɴ ᴋᴀᴍᴜ~"
                                    XeberlhynAJS.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, Terhormat)
                            if ThePeopleTeamBOTS.startswith("sbadd: "):
                                if AreyouReady in Creators:
                                   PersetanBuatHatters = eval(ShirashiBOTSPeoplE.contentMetadata["MENTION"])
                                   PersetanBuatHatters["MENTIONEES"][0]["M"]
                                   MakhlukBiadaps = []
                                   for RealMadridBosku in PersetanBuatHatters["MENTIONEES"]:
                                      MakhlukBiadaps.append(RealMadridBosku["M"])
                                   for MakhlukBiadap in MakhlukBiadaps:
                                      try:
                                          XeberlhynBoss.findAndAddContactsByMid(MakhlukBiadap)
                                          XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," "+str(XeberlhynBoss.getContact(MakhlukBiadap).displayName)+"~ Telah ditambahkan menjadi teman")
                                      except:XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," Gua limit add asyu ")
                            if ThePeopleTeamBOTS.startswith("sbinvite: "):
                                if AreyouReady in Creators:
                                   PersetanBuatHatters = eval(ShirashiBOTSPeoplE.contentMetadata["MENTION"])
                                   PersetanBuatHatters["MENTIONEES"][0]["M"]
                                   MakhlukBiadaps = []
                                   for RealMadridBosku in PersetanBuatHatters["MENTIONEES"]:
                                      MakhlukBiadaps.append(RealMadridBosku["M"])
                                   for MakhlukBiadap in MakhlukBiadaps:
                                      try:
                                          XeberlhynBoss.findAndAddContactsByMid(MakhlukBiadap)
                                          XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[MakhlukBiadap])
                                          XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," "+str(XeberlhynBoss.getContact(MakhlukBiadap).displayName)+"~ Telah ditambahkan menjadi teman")
                                      except:XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," Gua limit bosku")
                            if ThePeopleTeamBOTS.startswith("sbkick: "):
                                if AreyouReady in Creators:
                                   PersetanBuatHatters = eval(ShirashiBOTSPeoplE.contentMetadata["MENTION"])
                                   PersetanBuatHatters["MENTIONEES"][0]["M"]
                                   MakhlukBiadaps = []
                                   for RealMadridBosku in PersetanBuatHatters["MENTIONEES"]:
                                      MakhlukBiadaps.append(RealMadridBosku["M"])
                                   for MakhlukBiadap in MakhlukBiadaps:
                                      try:
                                          Bangsat["Daftarhitam"][MakhlukBiadap] = True
                                          XeberlhynBoss.TendanganMautiniBOSS(ByCreatorsBerlHyn, [MakhlukBiadap])
                                          XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," "+str(XeberlhynBoss.getContact(MakhlukBiadap).displayName)+"~ Telah dikeluarkan dari room")
                                      except:XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," Aku limit kick beb ")
                            if ThePeopleTeamBOTS.startswith("addbots: "):
                                if AreyouReady in Creators:
                                   PersetanBuatHatters = eval(ShirashiBOTSPeoplE.contentMetadata["MENTION"])
                                   PersetanBuatHatters["MENTIONEES"][0]["M"]
                                   MakhlukBiadaps = []
                                   for RealMadridBosku in PersetanBuatHatters["MENTIONEES"]:
                                      MakhlukBiadaps.append(RealMadridBosku["M"])
                                   for MakhlukBiadap in MakhlukBiadaps:
                                      try:
                                          Bangsat["Algojo"][MakhlukBiadap] = True
                                          XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," "+str(XeberlhynBoss.getContact(MakhlukBiadap).displayName)+"~ Telah ditambahkan dalam daftar bot")
                                      except:XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," Telah terdaftar didalam daftar jonli ")
                            if ThePeopleTeamBOTS.startswith("dellbots: "):
                                if AreyouReady in Creators:
                                   PersetanBuatHatters = eval(ShirashiBOTSPeoplE.contentMetadata["MENTION"])
                                   PersetanBuatHatters["MENTIONEES"][0]["M"]
                                   MakhlukBiadaps = []
                                   for RealMadridBosku in PersetanBuatHatters["MENTIONEES"]:
                                      MakhlukBiadaps.append(RealMadridBosku["M"])
                                   for MakhlukBiadap in MakhlukBiadaps:
                                      try:
                                          del Bangsat["Algojo"][MakhlukBiadap]
                                          XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," "+str(XeberlhynBoss.getContact(MakhlukBiadap).displayName)+"~ Telah dikeluarkan dari daftar bot")
                                      except:XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn," Belum terdaftar didalam daftar jonli ")
                            if ThePeopleTeamBOTS == "daftarbot":
                                if AreyouReady in Creators:
                                    if Bangsat["Algojo"] == {}:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn,"「Tidak ada bot yang terdaftar」")
                                    else:
                                        num = 1
                                        BangsatmahBebasCok = "= Daftar bot ="
                                        for ManusiaBajinganAsyu in Bangsat["Algojo"]:
                                            BangsatmahBebasCok += "\n• %i.  %s" % (num, XeberlhynBoss.getContact(ManusiaBajinganAsyu).displayName)
                                            num = (num+1)
                                        BangsatmahBebasCok += "\ntotal 「%i」 bot" % len(Bangsat["Algojo"])
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, BangsatmahBebasCok)
                            if ThePeopleTeamBOTS == "blacklist":
                                if AreyouReady in Creators:
                                    if Bangsat["Daftarhitam"] == {}:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn,"「Tidak ada daftar blacklist」")
                                    else:
                                        num = 1
                                        BangsatmahBebasCok = "= Daftar blacklist bot ="
                                        for ManusiaBajinganAsyu in Bangsat["Daftarhitam"]:
                                            BangsatmahBebasCok += "\n• %i.  %s" % (num, XeberlhynBoss.getContact(ManusiaBajinganAsyu).displayName)
                                            num = (num+1)
                                        BangsatmahBebasCok += "\ntotal 「%i」blacklist bot" % len(Bangsat["Daftarhitam"])
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, BangsatmahBebasCok)
                            if ThePeopleTeamBOTS == "ceban":
                                if AreyouReady in Creators:
                                    if Bangsat["Daftarhitam"] == {}:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn,"「ᴛɪᴅᴀᴋ ᴀᴅᴀ ꜱᴀᴍᴘᴀʜ ᴅɪꜱɪɴɪ!!!」")
                                    else:
                                        num = 1
                                        BangsatmahBebasCok = "= ꜱᴜᴋꜱᴇꜱ ᴍᴇɴɢʜᴀᴘᴜꜱ ꜱᴀᴍᴘᴀʜ!!! ="
                                        for ManusiaBajinganAsyu in Bangsat["Daftarhitam"]:
                                            BangsatmahBebasCok += "\n• %i.  %s" % (num, XeberlhynBoss.getContact(ManusiaBajinganAsyu).displayName)
                                            num = (num+1)
                                        BangsatmahBebasCok += "\ntotal 「%i」blacklist bot" % len(Bangsat["Daftarhitam"])
                                        Bangsat["Daftarhitam"] = {}
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, BangsatmahBebasCok)
                            if ThePeopleTeamBOTS.startswith("sbgantinama:"):
                                if AreyouReady in Creators:
                                    AyamJumbo = text.split(":")
                                    PapanNama = text.replace(AyamJumbo[0] + ":","")
                                    MariaOzawa = XeberlhynBoss.getProfile()
                                    MariaOzawa.displayName = str(PapanNama)
                                    XeberlhynBoss.updateProfile(MariaOzawa)
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "Selfbots sukses mengganti nama menjadi:\n{}".format(PapanNama))
                            if ThePeopleTeamBOTS.startswith("ajsgantinama:"):
                                if AreyouReady in Creators:
                                    AyamJumbo = text.split(":")
                                    PapanNama = text.replace(AyamJumbo[0] + ":","")
                                    MariaOzawa = XeberlhynAJS.getProfile()
                                    MariaOzawa.displayName = str(PapanNama)
                                    XeberlhynAJS.updateProfile(MariaOzawa)
                                    XeberlhynAJS.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "Antijs sukses mengganti nama menjadi:\n{}".format(PapanNama))
                            if ThePeopleTeamBOTS == "update picture":
                                if AreyouReady in Creators:
                                    Bangsat["SelfiPakeHandiCam"] = True
                                    XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Silahkan kirim foto profile bot nya」")
                            if ThePeopleTeamBOTS == "protectqr on":
                                if AreyouReady in Creators:
                                    if ClanSquadters in Bangsat["link"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectqr telah diaktifkan」")
                                    else:
                                        Bangsat["link"][ClanSquadters] = True
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengaktifkan Protectqr」")
                            if ThePeopleTeamBOTS == "protectqr off":
                                if AreyouReady in Creators:
                                    if ClanSquadters not in Bangsat["link"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectqr telah dinonaktifkan」")
                                    else:
                                        del Bangsat["link"][ClanSquadters]
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses menonaktifkan Protectqr」")
                            if ThePeopleTeamBOTS == "protectkick on":
                                if AreyouReady in Creators:
                                    if ClanSquadters in Bangsat["kickers"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectkick telah diaktifkan」")
                                    else:
                                        Bangsat["kickers"][ClanSquadters] = True
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengaktifkan protectkick」")
                            if ThePeopleTeamBOTS == "protectkick off":
                                if AreyouReady in Creators:
                                    if ClanSquadters not in Bangsat["kickers"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectkick telah dinonaktifkan」")
                                    else:
                                        del Bangsat["kickers"][ClanSquadters]
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses menonaktifkan protectkick」")
                            if ThePeopleTeamBOTS == "protectinv on":
                                if AreyouReady in Creators:
                                    if ClanSquadters in Bangsat["JeritanJanda"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectinvite telah diaktifkan」")
                                    else:
                                        Bangsat["JeritanJanda"][ClanSquadters] = True
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengaktifkan Protectinvite」")
                            if ThePeopleTeamBOTS == "protectinv off":
                                if AreyouReady in Creators:
                                    if ClanSquadters not in Bangsat["JeritanJanda"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectinvite telah dinonaktifkan」")
                                    else:
                                        del Bangsat["JeritanJanda"][ClanSquadters]
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses menonaktifkan Protectinvite」")
                            if ThePeopleTeamBOTS == "protectcancel on":
                                if AreyouReady in Creators:
                                    if ClanSquadters in Bangsat["paraundangan"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectcancel telah diaktifkan」")
                                    else:
                                        Bangsat["paraundangan"][ClanSquadters] = True
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengaktifkan Protectcancel」")
                            if ThePeopleTeamBOTS == "protectcancel off":
                                if AreyouReady in Creators:
                                    if ClanSquadters not in Bangsat["paraundangan"]:
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Protectcancel telah dinonaktifkan」")
                                    else:
                                        del Bangsat["paraundangan"][ClanSquadters]
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses menonaktifkan Protectcancel」")
                            if 'Protectantijs ' in ShirashiBOTSPeoplE.text:
                                if AreyouReady in Creators:
                                    DjancokbuatKlean = ShirashiBOTSPeoplE.text.replace('Protectantijs ','')
                                    if DjancokbuatKlean == 'on':
                                        if ClanSquadters in JandaBahenol:
                                            BacotsekaliAnda = "「Prorectantijs telah diaktifkan」"
                                        else:
                                            JandaBahenol.append(ClanSquadters)
                                            DudulKataKamvred = XeberlhynBoss.getGroup(ClanSquadters)
                                            BacotsekaliAnda = ""
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Prorectantijs telah diaktifkan」")
                                    elif DjancokbuatKlean == 'off':
                                        if ClanSquadters in JandaBahenol:
                                            JandaBahenol.remove(ClanSquadters)
                                            DudulKataKamvred = XeberlhynBoss.getGroup(ClanSquadters)
                                            BacotsekaliAnda = "「Prorectantijs telah diaktifkan」"
                                        else:
                                            BacotsekaliAnda = ""
                                        XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Prorectantijs telah dinonaktifkan」")
                if ShirashiBOTSPeoplE.contentType == 1:
                    if AreyouReady in Creators:
                        if Bangsat["SelfiPakeHandiCam"] == True:
                            LontePasarSenen = XeberlhynBoss.downloadObjectMsg(ShirashiBOTSPeoplE.id)
                            AwasAdaCorona = XeberlhynAJS.downloadObjectMsg(ShirashiBOTSPeoplE.id)
                            Bangsat["SelfiPakeHandiCam"] = False
                            XeberlhynBoss.updateProfilePicture(LontePasarSenen)
                            XeberlhynAJS.updateProfilePicture(AwasAdaCorona)
                            XeberlhynBoss.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengganti Foto profile」")
                            XeberlhynAJS.BecauseMyTeAmPEOPLEBOT(ByCreatorsBerlHyn, "「Sukses mengganti Foto profile」")
            except Exception as error:
                print (error)
        if TeamPeopleBoTS.type == 19: 
            if People in TeamPeopleBoTS.param3:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                    try:                                            
                        XeberlhynAJS.acceptGroupInvitation(TeamPeopleBoTS.param1)
                        G = XeberlhynAJS.getGroup(TeamPeopleBoTS.param1)
                        G.preventedJoinByTicket = False
                        XeberlhynAJS.updateGroup(G)
                        invsend = 0
                        SuratPanggilan = XeberlhynAJS.reissueGroupTicket(TeamPeopleBoTS.param1)
                        XeberlhynBoss.acceptGroupInvitationByTicket(TeamPeopleBoTS.param1,SuratPanggilan)
                        XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                    except:
                        try:
                            XeberlhynAJS.acceptGroupInvitation(TeamPeopleBoTS.param1)
                            G = XeberlhynAJS.getGroup(TeamPeopleBoTS.param1)
                            G.preventedJoinByTicket = False
                            XeberlhynAJS.updateGroup(G)
                            invsend = 0
                            SuratPanggilan = XeberlhynAJS.reissueGroupTicket(TeamPeopleBoTS.param1)
                            XeberlhynBoss.acceptGroupInvitationByTicket(TeamPeopleBoTS.param1,SuratPanggilan)
                            XeberlhynAJS.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            G.preventedJoinByTicket = True
                            XeberlhynAJS.updateGroup(G)
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            XeberlhynAJS.leaveGroup(TeamPeopleBoTS.param1)
                            XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[Berlin])
                        except:
                            pass
                else:pass
                return
            if Berlin in TeamPeopleBoTS.param3:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                    try:
                        G = XeberlhynBoss.getGroup(TeamPeopleBoTS.param1)
                        G.preventedJoinByTicket = False
                        XeberlhynBoss.updateGroup(G)
                        invsend = 0
                        SuratPanggilan = XeberlhynBoss.reissueGroupTicket(TeamPeopleBoTS.param1)
                        XeberlhynAJS.acceptGroupInvitationByTicket(TeamPeopleBoTS.param1,SuratPanggilan)
                        XeberlhynAJS.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                    except:
                        try:
                            G = XeberlhynBoss.getGroup(TeamPeopleBoTS.param1)
                            G.preventedJoinByTicket = False
                            XeberlhynBoss.updateGroup(G)
                            invsend = 0
                            SuratPanggilan = XeberlhynBoss.reissueGroupTicket(TeamPeopleBoTS.param1)
                            XeberlhynAJS.acceptGroupInvitationByTicket(TeamPeopleBoTS.param1,SuratPanggilan)
                            XeberlhynAJS.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            G.preventedJoinByTicket = True
                            XeberlhynAJS.updateGroup(G)
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                            XeberlhynAJS.leaveGroup(TeamPeopleBoTS.param1)
                            XeberlhynBoss.inviteIntoGroup(TeamPeopleBoTS.param1,[Berlin])
                        except:
                            pass
                else:pass
                return
        if TeamPeopleBoTS.type == 19:
            if TeamPeopleBoTS.param1 in Bangsat["kickers"]:
                if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                    Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                    XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
                else:
                    pass
        if TeamPeopleBoTS.type == 32:
            try:
                if TeamPeopleBoTS.param1 in Bangsat["paraundangan"]:
                    if TeamPeopleBoTS.param2 not in Creators and TeamPeopleBoTS.param2 not in Pasukan and TeamPeopleBoTS.param2 not in Bangsat["Algojo"]:
                        Bangsat["Daftarhitam"][TeamPeopleBoTS.param2] = True
                        if TeamPeopleBoTS.param3 not in Bangsat["Daftarhitam"]:
                            XeberlhynBoss.TendanganMautiniBOSS(TeamPeopleBoTS.param1,[TeamPeopleBoTS.param2])
            except:
                pass            
    except Exception as error:
        print (error)
while True:
    try:
        ByXeberlhyn = MyCreatorXeberlhyn.singleTrace(count=50)
        if ByXeberlhyn is not None:
            for TeamPeopleBoTS in ByXeberlhyn:
                MyCreatorXeberlhyn.setRevision(TeamPeopleBoTS.revision)
                thread = threading.Thread(target=BerlinLoveRieny, args=(TeamPeopleBoTS,))
                thread.start()
    except Exception as e:
        print(e)
